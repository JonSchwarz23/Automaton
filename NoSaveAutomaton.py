import turtle

def drawCircles(amount):
    turtle.penup()
    points = []
    turtle.goto(-400,0)
    count = 0
    while count < amount:
        turtle.pendown()
        turtle.circle(20)
        points = points + [[turtle.xcor(),turtle.ycor()+20]]
        turtle.penup()
        turtle.forward(80)
        count+=1
    return points

def lhNext(pointOne,label):
    turtle.setheading(0)
    turtle.goto(pointOne[0]+20,pointOne[1]-8)
    turtle.pendown()
    turtle.forward(40)
    turtle.penup()
    drawArrows()
    turtle.goto(pointOne[0]+20,pointOne[1]-20)
    turtle.setheading(0)
    turtle.forward(15)
    turtle.write(label, font=("Arial", 6, "normal"))

def hlNext(pointOne,label):
    turtle.setheading(180)
    turtle.goto(pointOne[0]-20,pointOne[1]+8)
    turtle.pendown()
    turtle.forward(40)
    turtle.penup()
    drawArrows()
    turtle.goto(pointOne[0]-20,pointOne[1]+8)
    turtle.setheading(180)
    turtle.forward(15)
    turtle.write(label, font=("Arial", 6, "normal"))

def lhNotNext(pointOne, pointTwo, label, distance):
    chart = [0,0,45,85,135,195,265,345]
    turtle.goto(pointOne[0]+12,pointOne[1]-16)
    turtle.pendown()
    middle = [(pointOne[0]+pointTwo[0])/2,pointOne[1]-chart[distance]]
    turtle.goto((pointOne[0]+pointTwo[0])/2,pointOne[1]-chart[distance])
    turtle.setheading(turtle.towards(pointTwo[0]-12,pointTwo[1]-16))
    turtle.goto(pointTwo[0]-12,pointTwo[1]-16)
    turtle.penup()
    drawArrows()
    turtle.setheading(0)
    turtle.goto(middle[0]-3,middle[1]-10)
    turtle.write(label, font=("Arial", 6, "normal"))
    
def hlNotNext(pointOne, pointTwo, label, distance):
    chart = [0,0,45,85,135,195,265,345]
    turtle.goto(pointOne[0]-12,pointOne[1]+16)
    turtle.pendown()
    middle = [(pointOne[0]+pointTwo[0])/2,pointOne[1]+chart[distance]]
    turtle.goto((pointOne[0]+pointTwo[0])/2,pointOne[1]+chart[distance])
    turtle.setheading(turtle.towards(pointTwo[0]+12,pointTwo[1]+16))
    turtle.goto(pointTwo[0]+12,pointTwo[1]+16)
    turtle.penup()
    drawArrows()
    turtle.setheading(180)
    turtle.goto(middle[0]-5,middle[1])
    turtle.write(label, font=("Arial", 6, "normal"))

def self(pointOne,label):
    turtle.goto(pointOne[0]-8,pointOne[1]-20)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(16)
    turtle.setheading(0)
    turtle.forward(16)
    turtle.setheading(90)
    turtle.forward(16)
    turtle.penup()
    drawArrows()
    turtle.setheading(0)
    turtle.goto(pointOne[0]-5,pointOne[1]-36)
    turtle.write(label,font=("Arial", 6, "normal"))

def entrance(pointOne):
    turtle.goto(pointOne[0], pointOne[1]+36)
    turtle.setheading(270)
    turtle.pendown()
    turtle.forward(15)
    turtle.penup()
    drawArrows()

def final(pointOne):
    turtle.setheading(0)
    turtle.goto(pointOne[0],pointOne[1]-15)
    turtle.pendown()
    turtle.circle(15)
    turtle.penup()
    
def drawArrows():
    turtle.pendown()
    turtle.right(135)
    turtle.forward(5)
    turtle.backward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.penup()

def labelNodes(numberOfNodes):
    i = 1
    while i <= numberOfNodes:
        turtle.goto((-400+80*(i-1))-5,15)
        turtle.write("Q" + str(i))
        i+=1

def addLine(i,j,label):
    if i == j:
        self([-400 + 80 * i,20],label)
    elif i > j:
        if j+1 == i:
            hlNext([-400 + 80 * i,20],label)
        else:
            hlNotNext([-400 + 80 * i,20],[-400 + 80 * j,20],label,i-j)
    else:
        if i+1 == j:
            lhNext([-400 + 80 * i,20],label)
        else:
            lhNotNext([-400 + 80 * i,20],[-400 + 80 * j,20],label,j-1)

def transitions(myInput):
    start = myInput[1:3]
    label = ""
    for x in myInput[4:]:
        if x == ")":
            break
        else:
            label = label + x
    end = myInput[-2:]
    return [start, label, end]

def __main__():
    turtle.ht()
    nodes = []
    while True:
        numberOfNodes = int(raw_input("Number of nodes (Max = 8): "))
        if numberOfNodes > 8 or numberOfNodes <= 1:
            print "The amount of nodes must be a number between 2 and 8."
        else:
            drawCircles(numberOfNodes)
            i = 1
            while i <= numberOfNodes:
                nodes = nodes + ["Q" + str(i)]
                i+=1
            break
    labelNodes(numberOfNodes)
    while True:
        startingNode = str(raw_input("Starting node: "))
        if startingNode in nodes:
            entrance([-400 + 80 * nodes.index(startingNode),20])
            break
        else:
            print "That node does not exist please choose a node between Q1 and Q" + str(numberOfNodes) + "."
    while True:
        endingNodes = str(raw_input("Accepting state (Enter all accepting states put a comma between them ex. Q1,Q3): "))
        endingNodes = endingNodes.split(",")
        valid = True
        for x in endingNodes:
            if x not in nodes:
                valid = False
                break
        if valid == True:
            for x in endingNodes:
                final([-400 + 80 * nodes.index(x),20])
            break
        else:
            print "One of those nodes does not exist please try again"
    addT = "Jonathan"
    print "Transitions(Enter one transtion then press enter. After the last transition press enter twice. Format (StartingNode,Letter)=EndingNode *No spaces*)"
    while True:
        addT = str(raw_input())
        if addT == "":
            break
        else:
            new = transitions(addT)
            if new[0] in nodes and new[2] in nodes:
                addLine(nodes.index(new[0]),nodes.index(new[2]),new[1])
            else:
                print "Looks like their was an error with your format. Please try again."
    saveImg()
            

if __name__ == "__main__":
    __main__()
    
   

    

    
