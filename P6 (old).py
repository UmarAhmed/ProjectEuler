#P6, This was way too easy
def sq():
    squares = []
    for i in range(1,101):
        squares.append(i**2)
    y = sum(range(1,101))
    print (y**2 - sum(squares)) 

sq()
