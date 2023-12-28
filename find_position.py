import math

i = int(input())
result = []


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def focus_distance(p1, p2):
    fd = math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
    return fd


def find_contact(fd, rd):
    if (fd > rd) or (fd < rd2) or (fd == 0 and r1 != r2):
        return 0
    elif (fd == 0 and r2 == r1):
        return -1
    elif (fd == rd or fd == rd2):
        return 1
    elif (rd2 < fd < rd):
        return 2


for _ in range(i):
    position = map(int, input().split(' '))
    x1, y1, r1, x2, y2, r2 = position
    if ((-10000 <= x1 <= 10000 and -10000 <= x2 <= 10000
            and -10000 <= y1 <= 10000 and -10000 <= y2 <= 10000)
            and (1 <= r1 <= 10000 and 1 <= r2 <= 10000)):

        p1 = Point2D(x=x1, y=y1)
        p2 = Point2D(x=x2, y=y2)
        fd = focus_distance(p1, p2)
        rd = r2+r1
        rd2 = abs(r1-r2)

        result.append(find_contact(fd, rd))


for j in result:
    print(j)
