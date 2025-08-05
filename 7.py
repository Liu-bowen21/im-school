def check_in_borders(n, x, y, l, orientation):
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

       
check_in_borders(n, x, y, l, orientation)