class Notebook:
    def __init__(self):
        self.CPU = ""
        self.GPU = ""
        self.RAM = ""
        self.DISPLAY = ""
        self.STORAGE = ""
        self.OS = ""

    # display object attribute
    def notebook_info(self):
        print(f'CPU:{self.CPU} GPU:{self.GPU} RAM:{self.RAM} DISPLAY:{self.DISPLAY} STORAGE:{self.STORAGE} OS:{self.OS}')

std = []
n = int(input('How many notebook? : '))
for i in range(n):
    s = Notebook()
    print(f"Please, Enter CPU info {i + 1}:")
    s.CPU = input("Enter CPU: ")
    s.GPU = input("Enter GPU: ")
    s.RAM = input("Enter RAM: ")
    s.DISPLAY = input("Enter DISPLAY: ")
    s.STORAGE = input("Enter STORAGE: ")
    s.OS = input("Enter OS: ")
    std.append(s)

# display all student in list
for i in std:
    i.notebook_info()
