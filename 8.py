class Ship():
    def __init__(self, length, x_pos, y_pos, direction):
        self.length = length
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction
    def getLength(self):
        return self.length
    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos
    def getDirection(self):
        return self.direction


class Battlefield:
    def __init__(self, length):
        self.length = length
        self.grid = self.initialisegrid()


    def displaygrid(self):
        for x in range(length):
            print()
            print(self.grid[x])
            print()
           


    def initialisegrid(self):
        p1bf = []
        for x in range(self.length):
            tmp = []
            for y in range(self.length):
                tmp.append("?")


            p1bf.append(tmp)
        return p1bf
   
    def listships(self):
        for i in range(len(self.shiplist)):
            print()
            print(f"Ship number {i+1}")
            print(f"Length: {self.shiplist[i].getLength()}")
            print(f"X Coordinate: {self.shiplist[i].getX()}")
            print(f"y Coordinate: {self.shiplist[i].getY()}")
            print(f"direction: {self.shiplist[i].getDirection()}")
            print()


    def createships(self, n):
        shiplist = []
        for i in range(n):
            l = int(input(f"Insert the length of ship number {i+1}"))
            x = int(input(f"Insert the x coordinate of ship number {i+1}"))
            y = int(input(f"Insert the y coordinate of ship number {i+1}"))
            direction = str(input(f"Insert the direction of ship number {i+1}"))
            direction = direction.lower()
            ship = Ship(l, x, y, direction)
            shiplist.append(ship)
       
        self.shiplist = shiplist


   


   




length = int(input("Please input the length of the grid"))


b1 = Battlefield(length)
b1.displaygrid()
b1.createships(2)
b1.listships()






