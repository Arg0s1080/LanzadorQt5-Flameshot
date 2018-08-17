#!/usr/bin/python3


class CompilaUI:
    def __init__(self, entrada, salida):
        self.entrada = entrada
        self.salida = salida

    @staticmethod
    def ejecuta(entrada, salida):
        import subprocess

        argui = list()
        argui.insert(0, "pyuic5")
        argui.insert(1, entrada)
        argui.append("-o")
        argui.append(salida)

        proceso = subprocess.run(argui, stdout=subprocess.PIPE)

        print("-", proceso)



