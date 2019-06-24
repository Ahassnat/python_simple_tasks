class student():

    shap='round'
    avg=96.55

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def orbit(self):
        return f'the name is {self.name} and his gender {self.sex} '

    @classmethod
    def commons(cls):
        return f'the student is {cls.shap} '
    @classmethod
    def f(cls):
        return f'the avg is {cls.avg}'

    @staticmethod
    def rang(rang='the student range is 55.12'):
        return f'The rang is ::{rang}'

mark=student("mohamed",12,"male")
print(f'the name is {mark.name}')
print(f'the age of{mark.age}')
print(f'the sex is {mark.sex}')

print(mark.orbit())
print(student.shap)
print(student.commons())
print(student.f())
print(student.rang())
print(student.rang(rang="12"))
