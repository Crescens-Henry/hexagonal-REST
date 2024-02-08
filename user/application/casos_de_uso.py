import re

from arrow import get
from user.application.JWT.utils import get_hashed_password, verify_password
from user.domain.user import Usuario
from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv



class UserUseCases:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.usuarios_temporales = {}
        load_dotenv()

    def crear_usuario(self, nombre: str, email: str, password: str):
        usuario = Usuario(nombre, email, password)
        self.usuarios_temporales[usuario.uuid] = usuario
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
        
    def verificar_usuario(self, uuid: str):
        usuario = self.usuarios_temporales.pop(uuid, None)
        if usuario is not None:
            usuario.verificado = True
            usuario.password = get_hashed_password(usuario.password)
            self.repositorio.guardar(usuario)
            return True
        return False

    def obtener_usuarios(self):
        return self.repositorio.obtener_todos()

    def obtener_usuario(self, user_id: str):
        return self.repositorio.obtener(user_id)

    def actualizar_usuario(self, user_id: str, nombre: str, email: str, password: str):
        usuario = Usuario(nombre, email, password)
        return self.repositorio.actualizar(user_id, usuario)

    def eliminar_usuario(self, user_id: str):
        return self.repositorio.eliminar(user_id)
    
    def autenticar_usuario(self, email: str, password: str):
        usuario = self.repositorio.obtener_por_email(email)
        if usuario is not None:
            if isinstance(usuario, dict):
                password_valida = verify_password(password, usuario['password'])
            else:
                password_valida = verify_password(password, usuario.password)
            if password_valida:
                return usuario
        return None