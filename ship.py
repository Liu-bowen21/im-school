import os
import time


def clear_screen():
  """
  AI GENERATED CODE
  """
  # For Windows
  if os.name == 'nt':
    os.system('cls')
  # For macOS and Linux (os.name is 'posix')
  else:
    os.system('clear')


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
        self.lives = length
    def getLength(self):
        return self.length
    def getX(self):
        return self.x_pos
    def getY(self):
        return self.y_pos
    def getDirection(self):
        return self.direction
   
    def __str__(self):
        return f"ship (lives={self.lives})"




class Battlefield:
    def __init__(self, length):
        self.length = length
        self.grid = self.initialisegrid('?')
        self.shipgrid = self.initialisegrid(0)
        self.shiplist = []


    def is_game_over(self):
        for ship in self.shiplist:
            if ship.lives > 0:
                return False
        return True
   


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
            tmp = [str(element) for element in grid[x]]
            print(tmp)
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
        for i in range(n):
            l = int(input(f"Insert the length of ship number {i+1}: "))
            x = int(input(f"Insert the x coordinate of ship number {i+1}: "))
            y = int(input(f"Insert the y coordinate of ship number {i+1}: "))
            direction = str(input(f"Insert the direction of ship number {i+1}: "))
            direction = direction.lower()
            ship = Ship(l, x, y, direction)
            #TODO: Keep asking for a new ship until it's valid
            if check_in_borders(self.length, ship) is True and self.colcheck(ship) is True:
                self.shiplist.append(ship)
                self.placeship(ship)
            else:
                print("Not Valid!")
       
        return self.shiplist
   
    def colcheck(self, ship):
        x = ship.x_pos
        y = ship.y_pos
        length = ship.length
        direction = ship.direction


        if direction == 'up':
            for i in range(length):
                if self.shipgrid[y-i][x] == 1:
                    return False
        elif direction == 'down':
            for i in range(length):
                if self.shipgrid[y+i][x] == 1:
                    return False
        elif direction == 'left':
            for i in range(length):
                if self.shipgrid[y][x-i] == 1:
                    return False
        elif direction == 'right':
            for i in range(length):
                if self.shipgrid[y][x+i] == 1:
                    return False
        return True
   
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
                self.shipgrid[y-i][x] = ship
        elif direction == 'down':
            for i in range(length):
                self.shipgrid[y+i][x] = ship
        elif direction == 'left':
            for i in range(length):
                self.shipgrid[y][x-i] = ship
        elif direction == 'right':
            for i in range(length):
                self.shipgrid[y][x+i] = ship
        else:
            print("Direction not valid")
        return True


    def attack(self):
        """
        This method lets the player attack a location. Checks if they hit a ship.
        In that case, it returns True and changes the self.shipgrid with 'x' if hit, 'o' if not
        params:
        returns: True if hit, False otherwise
        """
        x = int(input('Where do you want to attack (x coordinate): '))
        y = int(input('Where do you want to attack (y coordinate): '))
        if not self.grid[y][x] == '?':
            print("Not valid!")
            return False
        if self.shipgrid[y][x] != 0:
            hit = True
            self.grid[y][x] = "x"
            self.shipgrid[y][x].lives -= 1
            if self.shipgrid[y][x].lives == 0:
                print("You sunk a ship!")
        else:
            hit = False
            self.grid[y][x] = 'o'    
           
        if hit == True and self.shipgrid[y][x].lives > 0:
            print("You hit a ship!")
        elif hit == False:
            print("Unfortunately, you did not hit a ship.")  
        return hit




clear_screen()
length = int(input("Please input the length of the grid\n"))
bf1 = Battlefield(length)
bf2 = Battlefield(length)


turn = 'player1'
game_over = False


print(turn)
n = int(input("How many ships do you want to create?\n"))
shiplist = bf1.createships(n)
for i in range(len(shiplist)):
    bf1.placeship(shiplist[i])
bf1.displaygrid(bf1.shipgrid)
time.sleep(3)
clear_screen()
turn = "player2"


print(turn)
n = int(input("How many ships do you want to create?\n"))
shiplist = bf2.createships(n)
for i in range(len(shiplist)):
    bf2.placeship(shiplist[i])
bf2.displaygrid(bf2.shipgrid)
time.sleep(3)
clear_screen()


# This for loop will be while game_over is False:
while game_over == False:
    if turn == 'player2':
        turn = 'player1'
        bf2.displaygrid(bf2.grid)
        print("Player 1")
        hit = bf2.attack()
        time.sleep(3)
        clear_screen()
        game_over = bf2.is_game_over()
        if game_over:
            print("Player 1 wins!")
    else:
        turn = 'player2'
        bf1.displaygrid(bf1.grid)
        print("Player 2")
        hit = bf1.attack()
        time.sleep(3)
        game_over = bf1.is_game_over()
        if game_over:
            print("Player 2 wins!")
            time.sleep(5)
        clear_screen()
