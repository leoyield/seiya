class Todict(object):
    def __init__(self, *name):
        self.name = name
    def to_dict(self, vctuple):
        vctuple = list(vctuple)
        if not isinstance(vctuple[0], int):
            vctuple[0] = round(float(vctuple[0]), 2)
        return {self.name[x]: y for x,y in enumerate(vctuple)}