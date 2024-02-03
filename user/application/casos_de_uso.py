from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import uuid
from user.domain.user import Usuario

class UserUseCases:
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def crear_usuario(self, nombre: str, email: str, password: str):
        usuario = Usuario(nombre, email, password)
        usuario_guardado = self.repositorio.guardar(usuario)

        token = str(uuid.uuid4())

        self.enviar_correo_verificacion(usuario, token)

        return usuario_guardado
    
    def enviar_correo_verificacion(self, usuario: Usuario, token: str):
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(usuario.email, usuario.password)

        mensaje = MIMEMultipart()
        mensaje['From'] = 'crescencio2003@gmail.com'
        mensaje['To'] = usuario.email
        mensaje['Subject'] = 'Verificación de correo electrónico'

        enlace_verificacion = f'http://tu_sitio_web.com/verificar?token={token}'
        cuerpo = f'Haz clic en el siguiente enlace para verificar tu correo electrónico: {enlace_verificacion}'
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        servidor.send_message(mensaje)
        servidor.quit()
        

    def obtener_usuarios(self):
        return self.repositorio.obtener_todos()

    def obtener_usuario(self, user_id: str):
        return self.repositorio.obtener(user_id)

    def actualizar_usuario(self, user_id: str, nombre: str, email: str, password: str):
        usuario = Usuario(nombre, email, password)
        return self.repositorio.actualizar(user_id, usuario)

    def eliminar_usuario(self, user_id: str):
        return self.repositorio.eliminar(user_id)
    
    