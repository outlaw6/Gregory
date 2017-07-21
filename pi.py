# Izracunavanje broja pi
# metodom Gregori Lajbnic metodom




n = 1.0
PI = ( 4 / n )
for x in range(1,200000000):
    if x % 2 == 0:

        n+=2
        PI = PI + ( 4/n)
        print "Unutar", PI,n,x               
        continue

    n+=2

    PI = PI - ( 4/n )
    print "Izvan", PI,n,x
    
