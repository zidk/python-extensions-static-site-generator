from ssg.hooks import process

@process
class Menu:

    def __init__(self, message):
        print(message)