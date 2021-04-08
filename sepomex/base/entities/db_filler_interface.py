from abc import ABCMeta, abstractmethod


class DBFillerInterface(metaclass=ABCMeta):
    """
    Clase padre de clases con las que se quiera poblar la base de datos
    Los que hereden de esta clase deben incluirse en el comando:
    cemac/base/management/commands/filldatabase.py
    """
    @abstractmethod
    def fill_database(self):
        raise NotImplementedError
