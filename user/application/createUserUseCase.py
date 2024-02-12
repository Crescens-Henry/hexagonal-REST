import os
from dotenv import load_dotenv
from user.domain.Entity.user import User
from email.message import EmailMessage
import smtplib
from user.infrastructure.security.utils import get_hashed_password


class CreateUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        load_dotenv()
        

    def crear_usuario(self, user: User):
        usuario_existente = self.repositorio.obtener_por_email(user.credentials.email)
        if usuario_existente is not None:
            return {"error": "El correo electrónico ya está en uso."}
        user.credentials.password = get_hashed_password(user.credentials.password)
        self.repositorio.guardar(user)
        self.enviar_email(user.credentials.email, user)
        return user
    
    def enviar_email(self, email, usuario):
        remitente = os.getenv("REMITENTE.EMAIL")
        destinatario = email
        mensaje = f"dele click al link para confirmar su correo: http://localhost:8001/verificar/{usuario.status.token_uuid}"
        
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Confirmacion de correo"
        email.set_content(mensaje)
        
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(remitente, os.getenv("PASS.GMAIL"))
        smtp.send_message(email)
        smtp.quit()