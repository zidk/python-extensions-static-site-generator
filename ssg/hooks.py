conversion_hooks = []
process_hooks = []
document_processors = {}

def conversion(cls):
    conversion_hooks.append(cls)
    return cls

def process(cls):
    process_hooks.append(cls)
    return cls

def stats(doctype):
    def decorator(cls):
        if doctype not in document_processors:
            document_processors[doctype] = []
        document_processors[doctype].append(cls)
        return cls
    return decorator