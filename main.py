class bs:
    def __init__(self, cmat):
        self.cmat = cmat

    def common_method(self):
        print(self.cmat)

class ch(bs):
    def __init__(self, cmat, exa):
        super().__init__(cmat)
        self.exa = exa
    def exclusive_method(self):
        print(self.exa)


child_object = ch("стандартній атрибут", "екслюзивні атрибут")
child_object.common_method()
child_object.exclusive_method()
