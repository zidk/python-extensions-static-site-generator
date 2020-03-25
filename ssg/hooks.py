conversion_hooks = []
process_hooks = []

def conversion(cls):
    conversion_hooks.append(cls)
    return cls

def process(cls):
    process_hooks.append(cls)
    return cls