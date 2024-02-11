import os
from dotenv import load_dotenv
from user.domain.entities.user import Usuario
from email.message import EmailMessage
import smtplib
from user.infrastructure.security.utils import get_hashed_password


class CreateUserUseCase:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        load_dotenv()
        

    def crear_usuario(self, nombre: str,last_name:str, cellphone:int, email: str, password: str):
        usuario_existente = self.repositorio.obtener_por_email(email)
        if usuario_existente is not None:
            return {"error": "El correo electrónico ya está en uso."}
        usuario = Usuario(nombre,last_name, cellphone, email, get_hashed_password(password)) 
        self.repositorio.guardar(usuario)
        self.enviar_email(email, usuario)
        return usuario
    
    def enviar_email(self, email, usuario):
        remitente = os.getenv("REMITENTE.EMAIL")
        destinatario = email
        mensaje = f"dele click al link para confirmar su correo: http://localhost:8001/verificar/{usuario.uuid}"
        
        email = EmailMessage()
        email["From"] = remitente
        email["To"] = destinatario
        email["Subject"] = "Confirmacion de correo"
        email.set_content(mensaje)
        
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(remitente, os.getenv("PASS.GMAIL"))
        smtp.send_message(email)
        smtp.quit()