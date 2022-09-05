class FileHandler:
    def __init__(self, buffer):
        self.buffer = buffer

    def save_buffer_to_file(self):
        file_name = self.get_file_name()
        text = self.buffer.get_buffer()
        with open("content/" + file_name, "w") as f:
            f.write(text)
        self.buffer.set_buffer("")
        print("Saved to file successfully")
        print("Buffer cleared")
        return text

    def get_file_name(self):
        file_name = input("Enter file name: ")
        return file_name
