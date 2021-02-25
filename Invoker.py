import Command


class Invoker:
    def __init__(self):
        self._comandos = []

    def almacenar(self, command: Command):
        self._comandos.append(command)

    def ejecutar_comandos(self):
        for command in self._comandos:
            command.execute()
