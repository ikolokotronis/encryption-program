from src.classes.Messenger import Messenger
from src.utils.ROT13 import ROT13
from src.utils.ROT47 import ROT47


class RotFactory:
    MODES = {"1": ROT13, "2": ROT47}

    @staticmethod
    def produce(choice):
        return RotFactory.MODES.get(choice, Messenger.no_such_option)()
