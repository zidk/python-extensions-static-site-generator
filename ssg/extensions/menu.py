from ssg import hooks, parsers


files = []

@hooks.register("collect_files")
def collect_files(source, site_parsers):
    local_parsers = [
        parser
        for parser in site_parsers
        if not isinstance(parser, parsers.ResourceParser)
    ]
    for path in source.rglob("*"):
        for parser in local_parsers:
            if parser.valid_file_ext(path.suffix):
                files.append(path)


@hooks.register("generate_menu")
def generate_menu(html, base_ext):

    menu = ["<ul>\n"]
    names = [path.stem for path in files]

    for name in names:
        link = '<li><a href="{}{}">{}</a></li>\n'.format(name, base_ext, name.title())
        menu.append(link)

    menu.append("</ul>\n")

    return "".join(menu) + html
