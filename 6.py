class Battlefield:
    def __init__(self, length):
        self.length = length
        self.grid = self.initialisegrid()


    def displaygrid(self):
        for x in range(length):
            print()
            print(self.grid[x])
           


    def initialisegrid(self):
        p1bf = []
        for x in range(self.length):
            tmp = []
            for y in range(self.length):
                tmp.append("?")


            p1bf.append(tmp)
        return p1bf
   


   




length = int(input("Please input the length of the grid"))


b1 = Battlefield(length)
b1.displaygrid()
