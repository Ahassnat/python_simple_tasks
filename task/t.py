class T:
    m={
    'wine':8,
    'beer':6,
    'food':5,
    'desert':3
    }

    def __init__(self):
        self.total=0
        self.items=[ ]

    def add(self,item):
        self.items.append(item)
        self.total += self.m[item]

    def print_pill(self,tax,service):
        tax=(tax/100)*self.total
        service=(service/100)*self.total
        total=tax+service+self.total

        for item in self.items:
            print(f'{item} for {self.m[item]}')

        print(f'{"TOTAL"} for {total}')
