class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        new_str = ''
        for i in self.my_list:
            new_str = new_str + str(i) + '\n'
        return new_str

    def __add__(self, other):
        new_list = []
        result = ''

        for i in range(len(self.my_list)):
            for j in range(len(self.my_list[i])):
                new_list.append(self.my_list[i][j] + other.my_list[i][j])
            result = result + str(new_list) + '\n'
            new_list = []
        return result


a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = Matrix([[10, 21, 32], [44, 5, 6], [77, 81, 9]])
print(a)
print(b)
print(a + b)
