from PyQt5 import QtWidgets, uic, QtCore, QtGui
from conexion import Conectar
import time
from chat import Chat
from generarPdf import Pdf

# iniciar aplicacion
app = QtWidgets.QApplication([])

# cargar archivos .ui

registrar = uic.loadUi('./vistas/ventanaRegistrar.ui')
login = uic.loadUi('./vistas/ventanaLogin.ui')
chatBot = uic.loadUi('./vistas/ventanaChatBot.ui')
consultarHistorial = uic.loadUi('./vistas/ventanaFechaConsulta.ui')


def gui_registrar():
    userName = registrar.txtUserName.text()
    edad = registrar.txtEdad.text()
    if (len(userName) == 0 or len(edad) == 0):
        registrar.labelError.setText('Favor complete todos los campos')
    else:
        crearUsuario = Conectar()
        crearUsuario.registrarUsuario(
            userName=userName, edad=edad)

        gui_iniciarSesion()


def gui_login():
    userName = login.txtUserName.text()
    if (len(userName) == 0):
        login.labelError.setText('Favor complete todos los campos')
    else:
        consultarUsuario = Conectar()
        usuario = consultarUsuario.consultarUsuariosPorUserName(
            userName=userName)
        if len(usuario) == 0:
            login.btnError.setText('Usuario no existe')
            # time.sleep(3)
            # login.btnError.setText('')
        else:
            gui_abrirChatBot(usuario=usuario[0][1])


def salir():
    app.exit()


def gui_iniciarSesion():
    registrar.hide()
    login.show()


def gui_ingresar_elementosChat():
    chat = Chat()

    user_input = chatBot.txtEnviar.text()
    chatBot.txtEnviar.setText('')
    chatBot.labelUser.setText(user_input)

    print(user_input)

    if user_input.lower() in ['salir', 'terminar']:
        chatBot.labelChat.setText('Fue un placer atenderte ¡Hasta pronto!')
        registrarChat = Conectar()
        conversation_history = ''
        for diccionario in Chat.conversation_history:
            for clave, valor in diccionario.items():
                conversation_history += f"{clave} - {valor}\n"

        registrarChat.registrarChat(
            userName=chatBot.labelNombreUsuario.text().lower(), chat=conversation_history)
        salir()
    else:
        hh = chat.abrir_chat(user_input=user_input)
        print(Chat.conversation_history)

        chatBot.labelChat.setText(hh)
    # crearLabel(hh)


def gui_abrirChatBot(usuario):
    login.hide()
    chatBot.labelNombreUsuario.setText(usuario.upper())
    chatBot.show()


def crearLabel(text):
    frame_chat_bot = chatBot.frameChatBot

    layout = QtWidgets.QVBoxLayout()

    label = QtWidgets.QLabel(text)
    label.setFixedHeight(35)
    label.setStyleSheet("background-color: rgb(153, 193, 241);\n"
                        "border-radius:10px;\n"
                        "border:none;\n"
                        "font: 75 12pt 'Arial';\n"
                        )
    layout.addWidget(label)
    frame_chat_bot.setLayout(layout)


def gui_abrirConsultaHistorial():
    chatBot.hide()
    consultarHistorial.labelNombreUsuario.setText(
        chatBot.labelNombreUsuario.text())
    consultarHistorial.show()


def gui_consultarHistorial():
    fechaConsulta = consultarHistorial.inputDate.date().toString("yyyy-MM-dd")
    email = consultarHistorial.txtEmail.text()

    if (len(fechaConsulta) == 0 or (email) == 0):
        consultarHistorial.labelError.setText(
            'Favor complete todos los campos')
    else:
        consultarChat = Conectar()
        chat = consultarChat.consultarChat(
            userName=chatBot.labelNombreUsuario.text(), fecha=fechaConsulta)

        if len(chat) == 0:
            consultarHistorial.labelError.setText(
                'No hay chats registrados en esa fecha')
            # time.sleep(3)
            # login.btnError.setText('')
        else:
            # gui_abrirChatBot(usuario=chatBot.labelNombreUsuario.text())
            pdf = Pdf()
            conversation_history = ''
            for diccionario in Chat.conversation_history:
                for clave, valor in diccionario.items():
                    conversation_history += f"{clave} - {valor}\n"

            pdf.generarPdf(conversation_history)


# Botones

# Registrar
registrar.btnRegistrar.clicked.connect(gui_registrar)
registrar.btnIniciarSesion.clicked.connect(gui_iniciarSesion)
registrar.btnSalir.clicked.connect(salir)

# Login
login.btnIngresar.clicked.connect(gui_login)
login.btnSalir.clicked.connect(salir)

# ChatBot
chatBot.btnHistorial.clicked.connect(
    gui_abrirConsultaHistorial)
chatBot.btnEnviar.clicked.connect(gui_ingresar_elementosChat)
chatBot.btnSalir.clicked.connect(salir)

# Historial
consultarHistorial.btnConsultar.clicked.connect(gui_consultarHistorial)
# consultarHistorial.btnSalir.clicked.connect(salir)


# ejecutable
registrar.show()
app.exec()
