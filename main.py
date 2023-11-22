import math
x=0.5
h=0.02
while x<=0.9:
    if x<0.6:
        y=math.cos(math.sqrt(x))
    elif 0.6<=x<0.7:
        y=1 / math.tan(math.radians(x))
    elif x>=0.7:
        y=math.atan(1 / (math.pow(x, 3)))
    print(y)
    x+= h