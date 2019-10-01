
def sanitize(string, code):
    return "".join([ c if c in code else "" for c in string ])