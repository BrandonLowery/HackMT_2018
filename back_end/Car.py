
class Car(object):
    def __init__(self,i, xi, yi):
        self.i = i
        self.x = xi
        self.y = yi
        self.start = xi
        self.tracks = []
        self.status = False
    def getStatus(self):
        return self.status
    def setStatus(self, T):
        self.status = T
    def getTracks(self):
        return self.tracks
    def getID(self):
        return self.i
    def getStart(self):
        return self.start
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,newx):
        self.x = newx
        
    def updateCords(self, xn):
        self.tracks.append(self.x)
        self.x = xn
        #self.y = yn
    def checkLine(self):
        start = self.getStart()
        current = self.getX()

        if start < 200 and current >270:
            self.setStatus(True)
            return True
    
