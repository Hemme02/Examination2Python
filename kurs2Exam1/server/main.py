from kurs2Exam1.server.GuiHandler import GuiHandler
from kurs2Exam1.server.SocketHandler import SocketHandler

socketHandler = SocketHandler()
guiHandler = GuiHandler(socketHandler)
socketHandler.setGuiHandler(guiHandler)

port = guiHandler.getPort()
resultOfBinding = socketHandler.startToAcceptConnection(port)

if resultOfBinding == "failed":
    guiHandler.showWarningMsg()
else:
    guiHandler.startGui()

