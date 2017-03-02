#!/usr/bin/python -u

SQUARE = [(2000,2000), (3000,2000), (3000,3000), (2000,3000)]
HEART = [(2000, 2000), (2250, 1800), (2500, 2000), (2750, 1800), (3000,2000), (2500, 3000)]

MULTIPLIER = 10

SHIP = [(1231, 2084),
        (1007, 1635),
        (2155, 1860),
        (2681, 3098),
        (1841, 2033),
        (2072, 782),
        (2457, 1385),
        (2072, 782),
        (1841, 2033),
        (2681, 3098),
        (2155, 1860),
        (1007, 1635)]


# SHIP = reversed(SHIP)

points = SQUARE
points = SHIP

x_offset = 0
y_offset = 0
increment = 0

print "r=30000"
print "e=1"
while True:
    for x, y in points:
        for _ in xrange(0, MULTIPLIER):
            print "s=%d,%d,4095,4095,1,1" % (x + x_offset, y + y_offset)
    x_offset = x_offset + increment
    y_offset = y_offset + increment

    if x_offset >= 500:
        increment = increment * -1
    elif x_offset <= 0:
        increment = increment * -1

