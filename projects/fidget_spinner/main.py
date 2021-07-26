from turtle import *
state={'turn':0}

# this will make the fidget to spin
def spinner():
    clear()
    angle=state['turn']/10
    right(angle) #it will move the fidget to clockwise direction becuase our angle is right
    forward(100)
    dot(120,'red')
    back(100)
    right(120) #for anticlock direction we have to move to left angle
    forward(100)
    dot(120,'blue')
    back(100)
    right(120)
    forward(100)
    dot(120,'yellow')
    back(100)
    right(120)
    update()


# this will change its state
def animate():
    if state['turn']>0:
        state['turn']-=1
    
    spinner()
    ontimer(animate,20)


# this will control the speed of the fidget
def flick():
    state['turn']+=100 #speed of the circle on pressing space button
    # this will control the speed of the fidget
    # it is very slow
tracer(False)
width(20)
onkey(flick,'space') #on pressing space key the spin will will move, the speed will increase on pressing space key
listen()
animate()
done()
# lets run it
# now press the space key 