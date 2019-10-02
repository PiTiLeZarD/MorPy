
def sanitize(string, code):
    return "".join([ c if c == ' ' or c in code else "" for c in string.lower() ])