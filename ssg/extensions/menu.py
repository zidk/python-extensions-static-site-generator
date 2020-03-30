from ssg.hooks import register

cache = None

@register("build_menu")
def build_menu(file_path):
    print(file_path)
