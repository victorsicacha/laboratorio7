
class Command:

    def __init__(self, instance):
        self.instance = instance

    def command(self):
        object_instance = self.instance

    def execute(self):
        pass


class Comandos:

    def command_get(self):
        pass

    def execute(self):
        print("{} {} {}".format("puedo", " imprimir ", "cosas"))


class ComandosSimples(Command):

    def __init__(self, instance):
        super().__init__(instance)
        self._receiver = None

    def execute(self):
        self._receiver.action()


class ComandosComplejos(Command):
    pass
