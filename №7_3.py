class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'Клетка с количеством ячеек: {self.number}'

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number / other.number))

    def __sub__(self, other):
        return 'Ошибка' if self.number < other.number else Cell(self.number - other.number)

    def make_order(self, quantity):
        row = ''
        for i in range(int(self.number / quantity)):
            row = row + ('*' * quantity + '\n')
        row = row + '*' * (self.number % quantity)
        return row


cell_1 = Cell(45)
cell_2 = Cell(20)
print(cell_1 + cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_1.make_order(11))
