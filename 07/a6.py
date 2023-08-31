# Was macht dieses Programm?
x = int(input("Eine Zahl bitte:"))
y = 1
l = []

if x <= 1000:
    while 2 * y <= x:
        if x % y == 0:
            l.append(y)
        y = y + 1
    l.append(x)
    print(l)

# x = 6: x ist nicht > 1000 also wird der while loop gestartet
# y*2 ist 2 also wird geschaut ob 6 / 1 einen Rest hat, hat es nicht also wird y(1) zu l hinzugefügt
# danach wiederholt sich das 2-mal mit den gleichen Ergebnissen und dann wird x nochmal zur Liste hinzugefügt
# also bei x = 6 ist l = [1, 2, 3, 6]
# bei 17 ist l = [1, 17]
