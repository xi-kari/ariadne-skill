# USER_SENTINEL: preserve this note exactly.
def greeting(name):
    return f"Hello, {name}!"

def allocate(day, availability):
    return sorted(availability.get(day, []))[:1]
