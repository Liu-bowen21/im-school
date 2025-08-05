def check_in_borders(n, ship):
    """
    This function makes sure that a ship is in the borders of the grid
    params:
    - n: length of grid
    - ship: ship to place
    returns:
    True if the ship is in the borders, False otherwise
    """
    x, y, l, orientation = ship.x_pos, ship.y_pos, ship.length, ship.direction
    if l > n:
        return False
    else:
        if orientation == 'up':
            if y - l >= 0:
                return True
            else:
                return False
        if orientation == 'down':
            if y + l <= n :
                return True
            else:
                return False
        if orientation == 'right':
            if x + l <= n:
                return True
            else:
                return False
        if orientation == 'left':
            if x - l >= n:
                return True
            else:
                return False


class Ship():
    def __init__(self, length, x_pos, y_pos, direction):
        self.length = length
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.direction = direction
        self.shiplist = []
    def getLength(self):
        return self.length
    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos
    def getDirection(self):
        return self.direction
   
    def __str__(self):
        return f"Ship: length={self.length}, x={self.x_pos}, y={self.y_pos}, direction={self.direction}"




class Battlefield:
    def __init__(self, length):
        self.length = length
        self.grid = self.initialisegrid('?')
        self.shipgrid = self.initialisegrid(0)
        self.shiplist = []


    def displaygrid(self, grid):
        """
        This method displays the input grid
        params:
        - grid 2D list
        returns:
        None
        """
        for x in range(length):
            print()
            print(grid[x])
            print()


    def initialisegrid(self, symbol):
        """
        This method creates a grid of size self.length x self.length
        and fills it with a symbol
        params:
         - symbol to fill the grid with (e.g. ? or 0)
         reutrns:
         - grid (2D list)
        """
        grid = []
        for x in range(self.length):
            tmp = []
            for y in range(self.length):
                tmp.append(symbol)
            grid.append(tmp)
        return grid
   
    def listships(self):
        """
        This method prints all ship information in self.shiplist
        params: None
        returns: None
        """
        for i in range(len(self.shiplist)):
            print()
            print(f"Ship number {i+1}")
            print(f"Length: {self.shiplist[i].getLength()}")
            print(f"X Coordinate: {self.shiplist[i].getX()}")
            print(f"y Coordinate: {self.shiplist[i].getY()}")
            print(f"direction: {self.shiplist[i].getDirection()}")
            print()


    def createships(self, n):
        """
        This method creates n ships according to user input parameters
        and returns a list containing them
        params:
        - n number of ships to create
        returns:
        shiplist list of ships
        """
        shiplist = []
        for i in range(n):
            l = int(input(f"Insert the length of ship number {i+1}"))
            x = int(input(f"Insert the x coordinate of ship number {i+1}"))
            y = int(input(f"Insert the y coordinate of ship number {i+1}"))
            direction = str(input(f"Insert the direction of ship number {i+1}"))
            direction = direction.lower()
            ship = Ship(l, x, y, direction)
            #TODO: Keep asking for a new ship until it's valid
            if check_in_borders(self.length, ship) is True:
                shiplist.append(ship)
                self.placeship(ship)
            else:
                print("Not Valid!")
       
        return shiplist
   
    def placeship(self, ship):
        """
        This method places a ship on the ship grid. Returns True if places succesfully, False otherwise
        params:
        - ship: the ship to place
        returns:
        - bool: True if succesful, False otherwise
        """
        x = ship.x_pos
        y = ship.y_pos
        length = ship.length
        direction = ship.direction


        if direction == 'up':
            for i in range(length):
                self.shipgrid[y-i][x] = 1
        elif direction == 'down':
            for i in range(length):
                self.shipgrid[y+i][x] = 1
        elif direction == 'left':
            for i in range(length):
                self.shipgrid[y][x-i] = 1
        elif direction == 'right':
            for i in range(length):
                self.shipgrid[y][x+i] = 1
        else:
            print("Direction not valid")
        return True


    def attack(self):
        x = input('Where do you want to attack (x coordinate): ')
        y = input('Where do you want to attack (y coordinate): ')
        if self.shipgrid[y][x] == 1:
            hit = True
            self.grid[y][x] = "x"
        else:
            hit = False
            self.grid[y][x] = 'o'      
        return hit




length = int(input("Please input the length of the grid"))
bf = Battlefield(length)


bf.createships(1)
bf.displaygrid(bf.grid)
bf.displaygrid(bf.shipgrid)




# turn = 'player2'
# game_over = False
# # This for loop will be while game_over is False:
# for i in range(10):
#    if turn == 'player2':
#        turn = 'player1'
#    else:
#        turn = 'player2'
#    print(turn)
