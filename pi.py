import Draw
import random
import math
import time

# this program simulates several approximations of pi. Monte-Carlo uses the class "point."
class Point(object):
    
    def __init__(self, initialX=0, initialY=0):
        self.__x = initialX
        self.__y = initialY
        
    def __str__(self): 
        return "("+str(self.__x)+", "+str(self.__y)+")"  
    
    def getX(self):        return self.__x   # getters
    def getY(self):        return self.__y
    
    def setX(self, newX):  self.__x = newX   # setters
    def setY(self, newY):  self.__y = newY
    
    def makeDuplicate(self): # copied from homework, not needed
        ans = Point(self.__x, self.__y)
        return ans    
        
    def distance(self, other):
        dx = self.__x - other.__x
        dy = self.__y - other.__y
        return (dx*dx + dy*dy) ** 0.5  
    
    def inCircle(self, other, radius): # important!
        return self.distance(other) < radius
    
    def draw(self):
        Draw.filledRect(self.getX(), self.getY(), 2, 2)
        
        
        
    
# This function designs an opening screen to display before the simulation. All should be self-explanatory. 
# Magic numbers used for ugly asthetic purposes. 
def openingScreen():

    Draw.setFontFamily('Times New Roman')    
    Draw.setBackground(Draw.LIGHT_GRAY) # White was hurting my eyes
    Draw.clear()
    Draw.setColor(Draw.RED)
    Draw.setFontBold(True)    
    Draw.setFontSize(30)
    Draw.string("Approximations of Pi:", 300, 50)
    Draw.string("Theorems Related to Randomness and Probabilities", 85, 100)
    Draw.setFontSize(8)        
    Draw.string("1", 965, 110)

    Draw.setFontBold(False)  
    Draw.setFontItalic(True)        
    Draw.setColor(Draw.BLACK) 
    Draw.setFontSize(8)
    Draw.string("1", 330, 160)
    Draw.setFontSize(15)
    Draw.setFontItalic(True)    
    Draw.string("Based on the work of Boris Gaurevich", 338, 160)
    
    Draw.setFontItalic(False)
    Draw.setColor(Draw.BLACK) 
    Draw.setFontSize(16)        
    Draw.string("Pi appears in several theorems that are more naturally related to the probability field." , 25, 200)
    Draw.string("This simulation will depict three such phenomena: ", 25, 225)
    Draw.string("\t1. Buffon's Needle: \n \t\t- If you drop a needle of length a on a floor of wood panels, each of length b, \n\t\t  the probability of it crossing a line between panels is 2a/πb.", 25, 275)
    Draw.string("\t2. Cesaro's Theorem: \n \t\t - The probability p of two randomly selected numbers less than n being coprime tends toward\n\t\t    6/π*π as n tends toward infinity.", 25, 350)
    Draw.string("\t3. Monte-Carlo: The Darts Game:\n \t\t - If you throw n darts at a target of radius 1/2 inscribed in a square,\n\t\t   the ratio of dats inside the target to the total number thrown is π/4.", 25, 425)
    
    Draw.setFontItalic(True)
    Draw.setColor(Draw.BLACK)
    Draw.setFontSize(15)        
    Draw.string('For more information, and for proofs of each theorem, visit "wwww.pi314.net."', 50, 525)    

    
    time.sleep(15)
    Draw.clear()


# Theorem of the Buffon's needle
    # Suppose we have a floor made of parallel strips of wood, each the same width 2b, and we drop a needle of length 2a onto the floor. 
    # The probability that the needle will lie across a line between two strips is 2a/pi*b
    
def Buffon():
    
    Draw.clear()
    
    b = 100                     # b is the length of a floor board. a is the length of a needle. 
    a = 75        
    x1 = b                      # This X1, Y1 starts the board, and creates a good referencce frame to be used later. Same for height and width.
    y1 = 200
    height = 250
    width = 8*b        

    # Header: 
    Draw.setFontFamily('Times New Roman')    
    Draw.setColor(Draw.RED)
    Draw.setFontBold(True)  
    Draw.setFontItalic(False)
    Draw.setFontSize(30) 
    Draw.string("Buffon's Approximation of Pi", 250, 25)
    Draw.setFontSize(22)
    Draw.setColor(Draw.BLACK)
    Draw.string("Probability of needle crossing line: ", 255, 100)        
    Draw.setFontSize(30) 
    Draw.string("2a", 705, 75)
    Draw.string("πb", 705, 115)
    Draw.line(695, 115, 760, 115)
    
    # Footer:         
    Draw.string("Approximation of Pi: ", 350, 550)
    
    Draw.setColor(Draw.BLUE)
    Draw.line(x1+b, y1+height+20, x1+2*b, y1+height+20)
    Draw.line(x1+b, y1+height+10, x1+b, y1+height+30)
    Draw.line(x1+2*b, y1+height+10, x1+2*b, y1+height+30)        
    Draw.string("b", x1+b*1.4, y1+height+25)
    
    Draw.setColor(Draw.RED)
    Draw.line(x1+b, y1+height+80, x1+b+a, y1+height+80)
    Draw.line(x1+b, y1+height+70, x1+b, y1+height+90)
    Draw.line(x1+b+a, y1+height+70, x1+b+a, y1+height+90)  
    Draw.string("a", x1+b*1.25, y1+height+85)
    Draw.setColor(Draw.BLACK)
    
    #Initial Board: sets up paneled floor for needles to fall on. 
    Draw.setColor(Draw.BLACK)
    Draw.rect(x1, y1, width, height)
    for i in range(1, 8):
            Draw.line(x1 + b*i, y1, x1 + b*i, y1+height)
            
    pi = 0                                      # pi starts at zero
    approx = Draw.string(str(pi), 750, 550)     # approx is a placeholder so we can delete the old pi and rewrite a new one
    shots = 0                                   # need shots because we aren't using every i (assume ratio will stay the same)
    hits = 0
    
    # Simulation: loop n times. 
    for i in range(500):
        
            Draw.setColor(Draw.RED)

            theta = random.randint(0, 360)                    # randomly choose angle, x, and y on board       
            x = random.randint(x1, x1+width) 
            y =  random.randint(y1, y1+height)
            
            if (y+a*math.sin(theta) >= y1 and
                x+a*math.cos(theta) >=x1 and
                y+a*math.sin(theta) <= y1+height and
                x+a*math.cos(theta) <=x1 + width):            # excludes x and y values that fall off the board
                    shots += 1
                    
                    if x//b != (x+a*math.cos(theta))//b:      # if start of needle isn't in same box as end of needle
                            hits += 1
                    Draw.line(x, y, x + a*math.cos(theta), y + a*math.sin(theta)) # Draws needle at set interval
                    time.sleep(.0625)   
            
                    #Every M times: update the estimate of pi       
                    if i%10 == 0 and hits>0:
                            Draw.delete(approx)
                            pi = round((shots*2*a)/(hits*b), 10) 
                            Draw.setColor(Draw.BLACK)
                            approx = Draw.string(str(pi), 750, 550)
    time.sleep(4)
    Draw.clear()
  
    
# Cesaro's theorem:
    #The probability of two randomly selected integers being coprime is 6/pi**2
    #If we choose two natural integers less than n, the probability Pn of them being coprime tends towards  when n tends towards infinity.
    
# Coprime code kindly provided by Prof. Broder:
def gcd(m, n):
    if n == 0: return m
    else: return gcd(n, m % n)

def Cesaro(): 
    Draw.clear()
    
    # title
    Draw.setFontFamily('Times New Roman')    
    Draw.setColor(Draw.BLACK)
    Draw.setFontBold(True)    
    Draw.setFontSize(30) 
    Draw.string("Cesaro's Theorem:", 100, 100)
    
    Draw.setFontItalic(True)        
    Draw.setColor(Draw.DARK_BLUE)    
    Draw.setFontSize(16) 
    Draw.string("The probability that two random \n numbers <= n are coprime is 6/π.", 100, 200) 
    Draw.setFontSize(8)
    Draw.string("2", 387, 225)    
    
    Draw.setFontItalic(False) 
    Draw.setFontSize(16)     
    Draw.setColor(Draw.RED)
    Draw.string("y = π", 350, 600-(100*math.pi))
    Draw.setColor(Draw.BLUE)
    Draw.string("n = 1000", 350, 400)
    Draw.setColor(Draw.GREEN)
    Draw.string("n = 10000", 350, 450)
    Draw.setColor(Draw.YELLOW)
    Draw.string("n = 1000000", 350, 500) 
    
    # Board
    Draw.setColor(Draw.BLACK)
    axis = 600
    Draw.line(500, 200, 500, axis)
    Draw.line(500, axis, 900, axis)
    Draw.setColor(Draw.RED)
    Draw.line(500, axis-(100*math.pi), 900,  axis-(100*math.pi)) 
    Draw.setColor(Draw.BLACK)
    Draw.setFontBold(False)
    Draw.string("Number of Experiments", 610, 650)
    
    # levels is a list to keep track of several things at once: 
    # 0. the max number n in each set, 1. number of coprimes, 2. approximations of pi, and 3. a color associated with each n
    
    levels = [[1000, 0, 0, Draw.BLUE], [10000, 0, 0, Draw.GREEN],[100000, 0, 0, Draw.YELLOW]]
    
    # loop through levels and do an experiment with each level 400 times: 
    # Are 2 random nums coprime? If yes, update coprime count, reevaluate pi, and connect old pi to new pi on graph. 
    for experiments in range(1, 400): # loops through all levels
        for level in levels:          # in each level, do an experiment. 
            num1 = random.randint(0, level[0])
            num2 = random.randint(0, level[0])
                
            if gcd(num1, num2) == 1:
                level[1] += 1
                
            if level[1] > 0:         # Don't divide by zero!
                pi = math.sqrt(6/(level[1]/experiments)) #based on theorem
                newY = axis - (pi*100) # this is new pi. different name so we can hold onto old pi until we graph. 
                Draw.setColor(level[3])# reset color for level
                Draw.line(500+experiments-1, level[2], 500+experiments, newY) # connect points
                level[2] = newY
                time.sleep(.01625)
    time.sleep(4)
    Draw.clear()    
    

# The Monte-Carlo Approximation   
    # Suppose we throw (without aiming!) n darts in a round target (of radius 1/2) inscribed in a square. 
    # We then count the proportion of darts in the circle over the total number of darts. 
    # This ratio tends towards the ratio of the area of the circle (Pi/4) over the area of the square (1) , that is Pi/4.
  
def MonteCarlo(): # function simulates situation explained above
    
    Draw.clear()  
    
    center = Point(500, 350)  # center is a placeholder. radius will be used to determine whether a point is inCircle
    radius = 200
    
    # Title:
    Draw.setFontFamily('Times New Roman')    
    Draw.setColor(Draw.BLUE)
    Draw.setFontBold(True)    
    Draw.setFontSize(30)     
    Draw.string("Monte Carlo's Approximation of Pi", center.getX()/2.5, 50) 
    time.sleep(2)
    
    # Board:
    Draw.rect(center.getX() - radius, center.getY() - radius, radius*2, radius*2)
    Draw.oval(center.getX() - radius, center.getY() - radius, radius*2, radius*2)
    Draw.string("Approximation of Pi: ", center.getX()/2.5, center.getY() + 275)
    approx = Draw.string(str(0), (center.getX() + 175)/2, center.getY() + 275) # initializes approximation of pi at zero, and is easily deleted to be changed. 
    
    Shots = 0          # keeps count of all the points we will create
    Hits = 0           # keeps count of all the points in circle
    pi = 0
    
    for i in range(10000): # creates new points and tests whether they are in the circle. Then draws all points. 
        
        p = Point()          
        p.setX((center.getX() - radius) + random.random()*radius*2) # X and Y values for the whole box are described by center-radius.  Multiplied by diameter. 
        p.setY((center.getY() - radius) + random.random()*radius*2)
        Shots +=1
        
        if p.inCircle(center, radius):
            Hits +=1
            Draw.setColor(Draw.RED)
            p.draw() 
        else: 
            Draw.setColor(Draw.BLUE)
            p.draw()
            
        if i%100 == 0 and Hits > 0:                                  # delete and reevaluate pi every 100 points. Don't divide by zero. 
            pi = round(Hits/Shots *4, 10) # Just for pretty
            Draw.delete(approx)
            approx = str(pi)
            Draw.setColor(Draw.BLUE)
            approx = Draw.string((approx), center.getX() + 90, center.getY() + 275)
            time.sleep(.0625)                                       # program should be watchable
            
    time.sleep(4)
    Draw.clear()
    
    
# calling all functions:

def main():
    Draw.setCanvasSize(1000, 750)
    openingScreen()
    Buffon()
    Cesaro()
    MonteCarlo()
    
main()