class Tap():
    mune={
    'wine': 10,
    'beer': 6,
    'cola': 3,
    'food': 15,
    'desrt': 5
    }

    def __init__(self):
        self.total=0
        self.items=[ ]

    def add(self,item):
        self.items.append(item)
        self.total += self.mune[item]

    def print_pill(self,tax,service):
        tax=(tax/100)*self.total
        service=(service/100)*self.total
        total=self.total+tax+service

        for item in self.items:
            print(f'{item} :: {self.mune[item]}')
        print(f'{"TOTAL"} for Each {total}')
