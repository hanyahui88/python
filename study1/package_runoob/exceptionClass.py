class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror:
    print(" net worker error")

print(Networkerror.__doc__)
