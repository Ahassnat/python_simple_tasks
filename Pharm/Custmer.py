class Px():
    med="drug"
    def __init__(self,name,age,sex,type):
        self.name=name
        self.age=age
        self.sex=sex
        self.type=type

    def n(self):
        return f'The Patient Name is {self.name}'

    @classmethod
    def mid(cls):
        return f'the tybe is {cls.med}'

    @staticmethod
    def state(ps="review the doctor"):
        return ps
