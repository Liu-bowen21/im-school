class Ship():
    def __init__(self, length, x_pos, y_pos):
        self.length = length
        self.x_pos = x_pos
        self.y_pos = y_pos
    def getLength(self):
        return self.length
    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos

shipList = []
def listShip():
    for i in range(len(shipList)):
        print(f"Ship number {i+1}")
        print(f"Length: {shipList[i].getLength()}")
        print(f"X Coordinate: {shipList[i].getX()}")
        print(f"y Coordinate: {shipList[i].getY()}")
        print()



def createShip(n):
    for i in range(n):
        l = int(input("Insert the length of your ship"))
        x = int(input("Insert the x coordinate of your ship"))
        y = int(input("Insert the y coordinate of your ship"))
        ship = Ship(l, x, y)
        shipList.append(ship)

createShip(3)
listShip()