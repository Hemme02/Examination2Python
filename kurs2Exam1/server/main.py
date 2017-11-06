from kurs2Exam1.server.SocketHandler import SocketHandler
from kurs2Exam1.server.TerminalServer import *
import _thread

socketHandler = SocketHandler()



port = get_port()
resultOfBinding = socketHandler.startToAcceptConnection(port)

if resultOfBinding == "failed":
    print('could not bind port')
else:
    pass

send_from_terminal(socketHandler)