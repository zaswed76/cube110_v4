






class But:
    _config = {"dir": None, "ext": ".png", "height": "25"}
    def __init__(self, name):
        self.name = name

    @classmethod
    def set_config(cls, opt, value):
        cls._config[opt] = value

    def set_icon(self):
        print(self._config["dir"] + "_" + self.name)


But.set_config("dir", "/dir")


b = But("b1")
b.dis()