from dataclasses import dataclass


@dataclass
class Buffer:
    def __init__(self, text):
        self.buffer = text

    def get_buffer(self):
        if self.buffer == '':
            return 'Buffer is empty'
        return self.buffer

    def set_buffer(self, text):
        self.buffer = text
        return self.buffer
