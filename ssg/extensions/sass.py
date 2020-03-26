from ssg.hooks import conversion

@conversion
class Sass:

    def __init__(self, message):
        print(message)