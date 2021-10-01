from datetime import datetime
from colorama import init, Fore
from abc import ABC, abstractmethod


init(autoreset=True)


class Logger(ABC):
    @abstractmethod
    def info(self, mensaje, valor):
        pass

    @abstractmethod
    def warning(self, mensaje, valor):
        pass

    @abstractmethod
    def error(self, mensaje, valor):
        pass

    @abstractmethod
    def debug(self, mensaje, valor):
        pass

class LoggerConsole(Logger):
    def info(self, mensaje, valor):
        print(datetime.now(),Fore.BLUE+'INFO:', mensaje, valor)

    def warning(self, mensaje, valor):
        print(datetime.now(), Fore.YELLOW+'WARN:', mensaje, valor)

    def error(self, mensaje, valor):
        print(datetime.now(),Fore.RED + 'ERR:', mensaje, valor)

    def debug(self, mensaje, valor):
        print(datetime.now(),Fore.GREEN + 'DEB:', mensaje, valor)


class LoggerEmail(Logger):
    def info(self, mensaje, valor):
        print('Enviando email...')

    def warning(self, mensaje, valor):
        print('Se encontró un warning')


    def error(self, mensaje, valor):
        print('Se encontró un error envianfo el mail')


    def debug(self, mensaje, valor):
        print('Debug')


class LoggerFactory(ABC):
    def getLogger(self, tipo):
        diccionario = {
            'c': LoggerConsole(),
            'f': LoggerFile(),
            'e': LoggerEmail()
                    }
        return diccionario[tipo]




class LoggerFactoryImpl(LoggerFactory):
    def getLogger(self, type_log):
        if type_log == 'c':
            l = LoggerConsole()
        elif type_log == 'f':
            l = LoggerFile()
        elif type_log == 'e':
            l = LoggerEmail()
        return l



class LoggerFile(Logger):
    def info(self, mensaje, valor):
        with open('file_log.txt','a') as file:
            log_out = (str(datetime.now()), 'INFO', mensaje + str(valor), '\n')
            file.writelines(log_out)

    def warning(self, mensaje, valor):
        with open('file_log.txt', 'a') as file:
            log_out = (str(datetime.now()), 'INFO', mensaje + str(valor), '\n')
            file.writelines(log_out)

    def error(self, mensaje, valor):
        with open('file_log.txt','a') as file:
            log_out = (str(datetime.now()), 'INFO', mensaje + str(valor), '\n')
            file.writelines(log_out)

    def debug(self, mensaje, valor):
        with open('file_log.txt','a') as file:
            log_out = (str(datetime.now()), 'INFO', mensaje + str(valor), '\n')
            file.writelines(log_out)


if __name__ == "__main__":
    type_log = input("Ingrese la letra \'c\' para salida por consola o la letra \'f\' para salida por archivo")
    logger = LoggerFactoryImpl().getLogger(type_log = type_log)
    logger.info('hola', (3))
    logger.warning('hola', (3))
    logger.error('hola', (3))
    logger.debug('hola', (3))

