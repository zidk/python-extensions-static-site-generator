conversion_hooks = []
process_hooks = []
documents = {}

def conversion(cls):
    conversion_hooks.append(cls)
    return cls

def process(cls):
    process_hooks.append(cls)
    return cls

def stats(doctype):
    def _stats(cls):
        if doctype not in documents:
            documents[doctype] = []
        documents[doctype].append(cls)
        return cls
    return _stats