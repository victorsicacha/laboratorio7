

import Command
import Invoker
import Receiver

invoker = Invoker.Invoker
receiver = Receiver.Receiver
concrete_command = Command.ComandosSimples(receiver)
invoker.almacenar(concrete_command)
invoker.ejecutar_comandos()