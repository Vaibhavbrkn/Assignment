"""Create the pattern using nested for loop in Python."""

star = 5

for i in range(1 , 2*star):
    if(i>5):
        print('*' * (2*star-i))
    else:
        print('*' * i)
