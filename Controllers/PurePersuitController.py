import Controllers.JoystickController
import pygame

class Point:
    def __init__(self, x,y ):
        self.x = x
        self.y = y
    def dot(self, point):
        return self.x * point.x + self.y * point.y
    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)
    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)
    def __str__(self):
        return str(self.x) + ", " + str(self.y)
    def __mul__(self, other):
        return Point(self.x * other, self.y * other)

    __rmul__ = __mul__


class PurePersuitController:
    def __init__(self, lookAhead):
        self.points = []
        self.lookAhead = lookAhead
        self.lookAheadPoint = None
        self.maxVelo = None
        self.jsTest = Controllers.JoystickController.JoystickController()
        return

    def addPoint(self, x, y):
        self.points.append(Point(x, y))

    def getLookAheadPoint(self, loc):

        # get closest path point
        distance = float("inf")
        closest = 0
        for i in range(len(self.points)-1, -1, -1):
            d = ((loc.x-self.points[i].x)**2+(loc.y-self.points[i].y)**2)**0.5
            if(d < distance):
                closest = i
                distance = d

        #print(str(self.points[closest]))

        #calculate lookahead using parametric subsitution to find intersections https://stackoverflow.com/questions/1073336/circle-line-segment-collision-detection-algorithm/1084899#1084899
        E = self.points[closest]
        L = self.points[closest+1]
        C = loc
        r = self.lookAhead
        d = L - E
        f = E - C

        a = d.dot(d)
        b = 2 * f.dot(d)
        c = f.dot(f) - r**2
        discriminant = b**2 - 4 * a * c
        if(discriminant < 0):
            print("does not intersect")
        else:
            discriminant = discriminant**0.5
            t1 = (-b - discriminant)/(2*a)
            t2 = (-b + discriminant)/(2*a)

            canidates = {}
            if(t1 >= 0 and t1 <= 1.0):
                canidates[t1] = E + d * t1
            if(t2 >= 0 and t2 <= 1.0):
                canidates[t2] = E + d * t2

            if(len(canidates.keys()) > 0):
                self.lookAheadPoint = canidates[max(canidates.keys())]
                return self.lookAheadPoint
            else:
                print("does not intersect")

        #alternatively, get lookahead by picking closest path point, then going one lookahead up that segment


    def removePassedPoints(self):
        return
    def update(self, pos): #optional param sim
        self.getLookAheadPoint(Point(pos[0], pos[1]))
        return self.jsTest.update()

    def visualDebug(self, g):

        for i in range(len(self.points)-1):
            p1 = g.translatePoint(self.points[i])
            p2 = g.translatePoint(self.points[i+1])
            pygame.draw.line(g.screen, (0, 255, 0), p1, p2, 4)

        pygame.draw.circle(g.screen, (0, 255, 255), g.translatePoint(self.lookAheadPoint), 4, 0)
        return
