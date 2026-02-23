
import turtle
from PIL import Image
import random
import time

#Notes:
#included play_games(s) inside direction functions b/c after prompts, movement stopped working. I don't think this is the correct solution so if you have ideas plz go ahead change!
#ask about importing tkinter
#for saving the house try extracting by getting the gif using "s.bgpic()" and then putting that through "Image."
#For HOUSE section "turtle.tracer(8,0) when attempting to drag, otherwise "none" (such as with a keystroke)
#Take onkey out of the function and remove mainloop, see how that works

#Screen Setup
s = turtle.Screen()
s.setup(width=1340, height=800)
s.screensize(1340, 760)
current_loc = 'middle'

count = 0 #for igloo rendering

exit_game_info = turtle.Turtle()
exit_game_info.hideturtle()
exit_game_info.penup()
exit_game_info.speed(10)

def game_setup():
    global gameStatus
    gameStatus = True
    exit_game_info.goto(-500,340)
    s.bgpic("Scenes/MIDDLE.gif")
    exit_game_info.write("Press 'Esc' to exit at any time", align="center", font = ("Comic Sans", 15, "normal"))
    duck.goto(-30,-320)

def load_screen(position):
    global current_loc, count
    duck.hideturtle()
    if position == 'left' and current_loc == 'middle':
        current_loc = 'left'
        duck.goto(650,-240)
        s.bgpic('Scenes/LEFT.gif')
        duck.showturtle()
    elif position == 'left' and current_loc == 'igloo':
        current_loc = 'left'
        duck.goto(-70,-220)
        count += 1
        instructions.clear()
        for i in placed_items:
            i.hideturtle()
        s.bgpic('Scenes/LEFT.gif')
        duck.showturtle()
    elif position == 'right':
        current_loc = 'right'
        duck.goto(-640,-340)
        s.bgpic('Scenes/RIGHT.gif')
        duck.showturtle()
    elif position == 'middle':
        if current_loc == 'right':
            current_loc = 'middle'
            duck.goto(640, -340)
            s.bgpic('Scenes/MIDDLE.gif')
            duck.showturtle()
        elif current_loc == 'left':
            current_loc = 'middle'
            duck.goto(-640, -340)
            s.bgpic('Scenes/MIDDLE.gif')
            duck.showturtle()
    elif position == 'igloo':
        current_loc = 'igloo'
        duck.goto(430,-240) #TEMP
        s.bgpic('Scenes/default_igloo_bg.gif')
        load_igloo_section()
    elif position == 'last_saved_igloo':
        current_loc = 'igloo' #could cause unforseen errors but I doubt it
        duck.goto(430,-240)
        s.bgpic('Scenes/default_igloo_bg.gif')
        for i in placed_items:
            i.showturtle()
        s.update()
        load_igloo_section()
    elif position == 'customization':
        current_loc = 'customization'
        enter_character_custom()
    elif position == 'duck_jitsu':
        current_loc = 'duck_jitsu'
        play_duckjitsu()
            
        
def go_left_a_screen():
    global count
    user_choice = 'placeholder'
    xcor_list = set() 
    ycor_list = set()
    for i in range(-150,20,10):
        xcor_list.add(i)
    for i in range (-340,-250,10):
        ycor_list.add(i)
    if (current_loc == 'right') and (duck.xcor() == -650) and (duck.ycor() in ycor_list):
        user_choice = turtle.textinput("Go left?","Would you like to go left? ('Ok' or 'Cancel')")
    elif (current_loc == 'left') and (duck.ycor() == -210) and (duck.xcor() in xcor_list):
            user_choice = turtle.textinput("Enter igloo?","Would you like to enter the igloo? ('Ok' or 'Cancel')")
    elif (current_loc == 'middle') and (duck.xcor() == -650) and (duck.ycor() in ycor_list):
        user_choice = turtle.textinput("Go left?","Would you like to go left? ('Ok' or 'Cancel')")
    else:
        return
    if user_choice == None:
        play_game()
    elif user_choice == '':
        user_choice = 'yes'
        if user_choice == 'yes' and current_loc == 'middle':
            load_screen('left')
            play_game()
        elif user_choice == 'yes' and current_loc == 'right':
            load_screen('middle')
            play_game()
        elif user_choice == 'yes' and current_loc == 'left':
            if count == 0:
                load_screen('igloo')
            elif count > 0:
                load_screen('last_saved_igloo')
    else:
        play_game()

def go_right_a_screen():
    user_choice = 'placeholder'
    ycor_list = set()
    xcor_list2 = set() 
    xcor_jitsu = set()
    ycor_jistsu = [-190,-200]
    
    for i in range(-330,-200,10):
        ycor_list.add(i)
    for i in range(-270,-170,10):
        ycor_list.add(i)
    for i in range(-340,250,10):
        ycor_list.add(i)
    for i in range(350,440,10):
        xcor_list2.add(i)
    for i in range(-110,-40,10):
        xcor_jitsu.add(i)
    
    if (current_loc == 'left') and (duck.xcor() == 660) and (duck.ycor() in ycor_list):
            user_choice = turtle.textinput("Go right?","Would you like to go right? ('Ok' or 'Cancel')")
    elif (current_loc == 'middle') and (duck.xcor() == 650) and (duck.ycor() in ycor_list):
        user_choice = turtle.textinput("Go right?","Would you like to go right? ('Ok' or 'Cancel')")
    elif (current_loc == 'igloo') and (duck.xcor() == 440) and (duck.ycor() in ycor_list):
        user_choice = turtle.textinput("Exit Igloo?","Would you like to go exit the igloo? ('Ok' or 'Cancel')")
    elif (current_loc == 'middle') and (duck.xcor() in xcor_list2) and (duck.ycor() == -180):
        user_choice = turtle.textinput("Customize?","Would you like to customize your duck? ('Ok' or 'Cancel')")
    elif (current_loc == 'right') and (duck.xcor() in xcor_jitsu) and (duck.ycor() in ycor_jistsu):
        user_choice = turtle.textinput("Play Duck-Jitsu?","Would you like to Play Duck-Jitsu? ('Ok' or 'Cancel')")
    else:
        return
    if user_choice == None:
        play_game()
    elif user_choice == '':
        user_choice = 'yes'
        if (user_choice == 'yes') and (current_loc == 'middle') and (duck.xcor() in xcor_list2) and (duck.ycor() == -180):
            load_screen('customization')
        elif user_choice == 'yes' and current_loc == 'middle':
            load_screen('right')
            play_game()
        elif user_choice == 'yes' and current_loc == 'left':
            load_screen('middle')
            play_game()
        elif user_choice == 'yes' and current_loc == 'igloo':
            load_screen('left')
            play_game()
        elif user_choice == 'yes' and current_loc == 'right':
            load_screen('duck_jitsu')
    else:
        play_game()

#Main Game Turtle (Duck)
turtle.addshape("Ducks/basic_duck.gif") 
duck = turtle.Turtle()
duck.penup()
duck.shape("Ducks/basic_duck.gif") 
s.update()

#Basic Movement

def move_up():
    s.tracer(1)
    if duck.ycor() < 340:  #by doing this, we can add a boundary to where the duck can go, 1000 is a placeholder
        if current_loc == 'left':
            if (duck.ycor() < -210):
                duck.sety(duck.ycor()+10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'igloo':
            if (duck.ycor() < 250):
                duck.sety(duck.ycor()+10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'middle':
            if (duck.ycor() < -180):
                duck.sety(duck.ycor()+10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'right':
            if (duck.ycor() < -80):
                duck.sety(duck.ycor()+10)
                go_left_a_screen()
                go_right_a_screen()
        else:
            duck.sety(duck.ycor()+10)
            go_left_a_screen()
            go_right_a_screen()

def move_down():
    s.tracer(1)
    if duck.ycor() > -340:
        if current_loc == 'left':
            if (duck.ycor() > -330):
                duck.sety(duck.ycor()-10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'igloo':
            if (duck.ycor() > -270):
                duck.sety(duck.ycor()-10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'middle':
            if (duck.ycor() > -340):
                duck.sety(duck.ycor()-10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'right':
            if (duck.ycor() > -340):
                duck.sety(duck.ycor()-10)
                go_left_a_screen()
                go_right_a_screen()
        else:
            duck.sety(duck.ycor()-10)
            go_left_a_screen()
            go_right_a_screen()

def move_left():
    s.tracer(1)
    if duck.xcor() > -660:
        if current_loc == 'left':
            if (duck.xcor() > -420):
                duck.setx(duck.xcor()-10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'igloo':
            if (duck.xcor() > -410):
                duck.setx(duck.xcor()-10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'middle':
            if (duck.xcor() > -650):
                duck.setx(duck.xcor()-10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'right':
            if (duck.xcor() > -650):
                duck.setx(duck.xcor()-10)
                go_left_a_screen()
                go_right_a_screen()
        else:
            duck.setx(duck.xcor()-10)
            go_left_a_screen()
            go_right_a_screen()

def move_right():
    s.tracer(1)
    if duck.xcor() < 660:
        if current_loc == 'left':
                duck.setx(duck.xcor()+10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'igloo':
            if (duck.xcor() < 440):
                duck.setx(duck.xcor()+10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'middle':
            if (duck.xcor() < 650):
                duck.setx(duck.xcor()+10)
                go_left_a_screen()
                go_right_a_screen()
        elif current_loc == 'right':
            if (duck.xcor() < 660):
                duck.setx(duck.xcor()+10)
                go_left_a_screen()
                go_right_a_screen()
        else:
            duck.setx(duck.xcor()+10)
            go_left_a_screen()
            go_right_a_screen()

#Assisting Functions


def exit_game():
    global gameStatus
    turtle.hideturtle()
    s.clear()
    gameStatus = False

############## HTIN's HOME SECTION ################
title = turtle.Turtle()
title.hideturtle()
title.penup()
instructions = turtle.Turtle()
instructions.hideturtle()
instructions.penup()
item = turtle.Turtle()
item.hideturtle()
item.penup()
placed_items = []
def load_igloo_section():
    global current_loc
    if count == 0:
        title.goto(0,50)
        instructions.goto(0,-200)
        title.write("Welcome. Let's customize your home!", align="center", font = ("Comic Sans", 24, "normal"))
        instructions.write("Press 'b' for bed, 't' for table, 'p' for plant, 'r' for rug, 's' for stool, 'v' for television, and 'c' for couch", align="center", font = ("Comic Sans", 18, "normal"))
    duck.showturtle()
    turtle.addshape("Furniture/fbed.gif")
    turtle.addshape("Furniture/fcouch.gif")
    turtle.addshape("Furniture/fplant.gif")
    turtle.addshape("Furniture/frug.gif")
    turtle.addshape("Furniture/fstool.gif")
    turtle.addshape("Furniture/ftable.gif")
    turtle.addshape("Furniture/ftv.gif")
    inventory = {"bed": "Furniture/fbed.gif", "table": "Furniture/ftable.gif", "plant": "Furniture/fplant.gif", "rug": "Furniture/frug.gif", "couch": "Furniture/fcouch.gif", "stool": "Furniture/fstool.gif","tv": "Furniture/ftv.gif"}
    
    def delete_item(target_item):
        if current_loc == 'igloo':
            if target_item in placed_items:
                target_item.hideturtle()
                placed_items.remove(target_item)
                s.update()

    def delete_all_items():
        if current_loc == 'igloo':
            while placed_items:
                item = placed_items.pop()
                item.hideturtle()
            s.update()

    def clear_title():
        title.clear()
        instructions.clear()
        instructions.goto(0,315)
        instructions.write("Press 'b' for bed, 't' for table, 'p' for plant, 'r' for rug, 's' for stool, 'v' for television, and 'c' for couch", align="center", font = ("Comic Sans", 15, "normal"))
        instructions.goto(0,285)
        instructions.write("Right click on an item to delete, press 'd' to delete all items", align="center", font = ("Comic Sans", 15, "normal"))
    s.ontimer(clear_title, 5000)
    s.update()
    def choose_item(itemx):
        if current_loc == 'igloo':
            item = turtle.Turtle()
            item.penup()
            item.shape(inventory[itemx])
            placed_items.append(item)
        def drag_item(x,y):
            if current_loc == 'igloo':
                if (-410 <= x <= 440) and (-270 <= y <= 250):
                    s.tracer(8,0)
                    item.goto(x,y)
        def right_click(x,y):
            delete_item(item)

        item.ondrag(drag_item)
        item.onclick(right_click, btn=3)

    def put_bed():
        s.tracer(1)
        choose_item("bed")
    def put_table():
        s.tracer(1)
        choose_item("table")
    def put_plant():
        s.tracer(1)
        choose_item("plant")
    def put_couch():
        s.tracer(1)
        choose_item("couch")
    def put_rug():
        s.tracer(1)
        choose_item("rug")
    def put_stool():
        s.tracer(1)
        choose_item("stool")
    def put_tv():
        s.tracer(1)
        choose_item("tv")



    s.onkey(put_bed, "b")
    s.onkey(put_table, "t")
    s.onkey(put_plant, "p")
    s.onkey(put_rug, "r")
    s.onkey(put_stool, "s")
    s.onkey(put_couch, "c")
    s.onkey(put_tv, "v")
    s.onkey(delete_all_items, "d")
    s.listen()
#################### END OF HOME SECTION ##################################

################### START OF JAKE's MINIGAME ############################## (Lets break it down!)
choices = ["fire", "snow", "water"]


turtle.addshape("Card/firetemp.gif")
turtle.addshape("Card/snowtemp.gif")
turtle.addshape("Card/watertemp.gif")
turtle.addshape("Card/question.gif")
turtle.addshape('Card/diagram.gif')
fin=turtle.Turtle()
fin.hideturtle()

winturtle=turtle.Turtle()
winturtle.hideturtle()
winturtle.penup()


wins=0
winvar=open("wins.txt", "r") 
filewins=winvar.read().strip() 
if filewins: 
    wins=int(filewins) 
winvar.close()



def finish(result):


    fin.penup()
    fin.goto(-100,-50)
    fin.clear()
    fin.write(f'You {result}',font=('Verdana',40,'normal'))
    

def cardopening():
    turtle.textinput('Hello!','Welcome to Duck-Jitsu! (press anything to continue)')
    turtle.textinput('Tutorial','Select a card by clicking on it')
    diagramturtle.showturtle()
    diagramturtle.shape('Card/diagram.gif')
    turtle.textinput('Tutorial','Fire beats Ice, Ice beats Water, and Water beats Fire')
    turtle.textinput('Tutorial','Good Luck!')
    diagramturtle.penup()
    diagramturtle.goto(0,300)

fire = turtle.Turtle()
snow = turtle.Turtle()
water = turtle.Turtle()
question=turtle.Turtle()
diagramturtle=turtle.Turtle()

fire.hideturtle()
snow.hideturtle()
water.hideturtle()
question.hideturtle()
diagramturtle.hideturtle()

fire.shape("Card/firetemp.gif")
snow.shape("Card/snowtemp.gif")
water.shape("Card/watertemp.gif")
question.shape("Card/question.gif")

def setup():
    fire.penup()
    fire.goto(-250, -175)
    fire.showturtle()

    snow.penup()
    snow.goto(0, -175)
    snow.showturtle()

    water.penup()
    water.goto(250, -175)
    water.showturtle()

    question.shape('Card/question.gif')
    question.penup()
    question.goto(0,150)
    fin.clear()

def updatewins():
    winturtle.clear()
    winturtle.goto(-550,175)
    winturtle.write(f'Wins: {wins}', font=('Verdana', 20, 'normal'))

def reveal(compchoice):
    if compchoice=='fire':
        question.shape('Card/firetemp.gif')
    elif compchoice=='snow':
        question.shape('Card/snowtemp.gif')
    elif compchoice=='water':
        question.shape('Card/watertemp.gif')




def play(playerchoice,turtlename):
    turtlename.goto(0,-175)
    question.goto(0,125)
    compchoice = random.choice(choices)
    reveal(compchoice)
    global wins
    if (playerchoice == "fire"):
        water.hideturtle()
        snow.hideturtle()
        if compchoice=='snow':
            result='win!'
            wins+=1
        elif compchoice=='fire':
            result='tied'
        elif compchoice=='water':
            result='lost'
    if (playerchoice == "water"):
        fire.hideturtle()
        snow.hideturtle()
        if compchoice=='fire':
            result='win!'
            wins+=1
        elif compchoice=='water':
            result='tied'
        elif compchoice=='snow':
            result='lost'
    if (playerchoice == "snow"):
        water.hideturtle()
        fire.hideturtle()
        if compchoice=='water':
            result='win!'
            wins+=1
        elif compchoice=='snow':
            result='tied'
        elif compchoice=='fire':
            result='lost'
    finish(result)
    updatewins()
    time.sleep(2)
    global againcard
    againcard=turtle.textinput('Again?','Do you want to play again? (Press Cancel to exit)')
    return result
def firechoice(x,y):
    if current_loc == 'duck_jitsu':
        play('fire',fire)
    
def snowchoice(x,y):
    if current_loc == 'duck_jitsu':
        play('snow',snow)
    
def waterchoice(x,y):
    if current_loc == 'duck_jitsu':
        play('water',water)
    


#Main
def play_duckjitsu():
    global againcard, current_loc
    s.bgpic("Scenes/duckjitsubg.gif")
    fire.showturtle()
    snow.showturtle()
    water.showturtle()
    question.showturtle()
    againcard='Y'
    cardopening()
    updatewins()
    while againcard!=None:
        setup()

        fire.onclick(firechoice)
        snow.onclick(snowchoice)   
        water.onclick(waterchoice)
    if againcard==None:
        fire.hideturtle()
        snow.hideturtle()
        water.hideturtle()
        question.hideturtle()
        diagramturtle.hideturtle()
        fin.clear()
        winturtle.clear()
        current_loc = 'right'
        s.bgpic('Scenes/RIGHT.gif')
        winlist = open("wins.txt", "w") 
        winlist.write(str(wins)) 
        winlist.close()
        duck.showturtle()
        play_game()
##################### END OF MINIGAME ###################################

##################### START OF JORGE'S CHARACTER CUSTOMIZATION ###########################
basic_duck = turtle.Turtle()
flower_duck = turtle.Turtle()
glasses_duck = turtle.Turtle()
heart_duck = turtle.Turtle()
leaf_duck = turtle.Turtle()
monacle_duck = turtle.Turtle()
tophat_duck = turtle.Turtle()
white_color_turtle = turtle.Turtle()

buttons = [basic_duck, flower_duck, glasses_duck, heart_duck, leaf_duck, monacle_duck, tophat_duck, white_color_turtle]
string_hat_buttons = ["basic_duck2x", "flower_duck2x", "glasses_duck2x", "heart_duck2x", "leaf_duck2x", "monacle_duck2x", "tophat_duck2x"]
string_color_buttons = ["RED", "ORANGE", "YELLOW", "GREEN", "BLUE", "PINK", "VIOLET"]

#Main Game Turtle (Duck)
drawing_turtle = turtle.Turtle()
drawing_turtle.hideturtle()
drawing_turtle.penup()
drawing_turtle.speed(10)
                                         #Moved, shouldn't affect anything
writing_turtle = turtle.Turtle()
writing_turtle.hideturtle()
writing_turtle.penup()
writing_turtle.speed(10)
#Accessories
turtle.addshape("Ducks/basic_duck.gif")
turtle.addshape("Ducks/flower_duck.gif")
turtle.addshape("Ducks/glasses_duck.gif")
turtle.addshape("Ducks/heart_duck.gif")     #NEW
turtle.addshape("Ducks/leaf_duck.gif")
turtle.addshape("Ducks/monacle_duck.gif")
turtle.addshape("Ducks/tophat_duck.gif")
#Colors
turtle.addshape("Colors/BLUE.gif")
turtle.addshape("Colors/GREEN.gif")
turtle.addshape("Colors/ORANGE.gif")
turtle.addshape("Colors/PINK.gif")     #NEW
turtle.addshape("Colors/RED.gif")
turtle.addshape("Colors/VIOLET.gif")
turtle.addshape("Colors/WHITE.gif")
turtle.addshape("Colors/YELLOW.gif")


#Resizes
turtle.addshape("DucksIconsLarge/basic_duck2x.gif")
turtle.addshape("DucksIconsLarge/flower_duck2x.gif")
turtle.addshape("DucksIconsLarge/glasses_duck2x.gif")
turtle.addshape("DucksIconsLarge/heart_duck2x.gif")     #NEW
turtle.addshape("DucksIconsLarge/leaf_duck2x.gif")
turtle.addshape("DucksIconsLarge/monacle_duck2x.gif")
turtle.addshape("DucksIconsLarge/tophat_duck2x.gif")

turtle.addshape("user_duck.gif")

def draw_continue_button(x,y,text):
    drawing_turtle.penup()
    drawing_turtle.color("black")
    drawing_turtle.pensize(1)
    drawing_turtle.hideturtle()
    drawing_turtle.setheading(0)
    drawing_turtle.goto(x, y)
    drawing_turtle.pendown()
    drawing_turtle.fillcolor('grey')
    drawing_turtle.begin_fill()
    for i in range(2):
        drawing_turtle.forward(170)
        drawing_turtle.right(90)
        drawing_turtle.forward(50)
        drawing_turtle.right(90)
    drawing_turtle.end_fill()
    drawing_turtle.penup()
    writing_turtle.goto(drawing_turtle.xcor()+85, drawing_turtle.ycor()-45)
    writing_turtle.write(text, False, align="center", font=("Comic Sans MS", 25, 'bold'))


s.listen()
#NEW

step = 'introduction'  #this may be a source of problems
def location_of_click(x,y):
    global step, tempCondition, current_loc
    if current_loc == 'customization':
        if step == 'introduction':
            if (-60 <= x <= 110) and (-70 <= y <= -20):  #(inputed x <= x <= x+170) and (y-50 <= y <= inputted y) inputted = variables given to draw_continue_button
                step = 'hats'
                hat_screen() #do code here after they press continue
        elif step == 'hats':
            if (450 <= x <= 620) and (-320 <= y <= -270):   #(450, -270)
                step = 'colors'
                color_select_screen()
        elif step == 'colors':
            if (450 <= x <= 620) and (-320 <= y <= -270):  #(450, -270)
                step = 'final_screen'
                final_screen()
        elif step == 'final_screen':
            if (150 <= x <= 320) and (-50 <= y <= 0):  #(150, 0)
                clear_turtles()
                model_duck.hideturtle()
                enter_character_custom()
            elif (-330 <= x <= -160) and (-50 <= y <= 0):  #(-330, 0)
                model_duck.hideturtle()
                clear_turtles()
                tempCondition = False
                step = 'done'
                current_loc = 'middle'
                s.bgpic('Scenes/MIDDLE.gif')
                duck.showturtle()
                play_game()


def hat_screen():
    clear_turtles()
    writing_turtle.goto(0,200)
    writing_turtle.write("Select your accessory!", False, align="center", font=("Comic Sans MS", 30, 'bold'))
    setup_buttons("DucksIconsLarge/",string_hat_buttons)
    draw_continue_button(450, -270, "Continue")
    model_duck.goto(-290,-40)
    drawing_turtle.goto(-250,-50)
    drawing_turtle.setheading(0)
    drawing_turtle.forward(100)
    drawing_turtle.setheading(90)
    #Box around model
    drawing_turtle.pendown()
    drawing_turtle.color("beige")
    drawing_turtle.pensize(5)
    drawing_turtle.forward(150)
    drawing_turtle.left(90)
    drawing_turtle.forward(300)
    drawing_turtle.left(90)
    drawing_turtle.forward(300)
    drawing_turtle.left(90)
    drawing_turtle.forward(300)
    drawing_turtle.left(90)
    drawing_turtle.forward(150)
    drawing_turtle.penup()
    model_duck.showturtle()
    s.update()

    
def color_select_screen():
    clear_turtles()
    writing_turtle.goto(0,200)
    writing_turtle.write("Select your color!", False, align="center", font=("Comic Sans MS", 30, 'bold'))
    setup_buttons("Colors/", string_color_buttons)
    draw_continue_button(450, -270, "Continue")
    drawing_turtle.goto(-250,-50)
    drawing_turtle.setheading(0)
    drawing_turtle.forward(100)
    drawing_turtle.setheading(90)
    #Box around model
    drawing_turtle.pendown()
    drawing_turtle.color("beige")
    drawing_turtle.pensize(5)
    drawing_turtle.forward(150)
    drawing_turtle.left(90)
    drawing_turtle.forward(300)
    drawing_turtle.left(90)
    drawing_turtle.forward(300)
    drawing_turtle.left(90)
    drawing_turtle.forward(300)
    drawing_turtle.left(90)
    drawing_turtle.forward(150)
    drawing_turtle.penup()

def final_screen():
    clear_turtles()
    hide_turtles()
    model_duck.goto(0,0)
    writing_turtle.goto(0,200)
    writing_turtle.write("Are you happy with your duck?", False, align="center", font=("Comic Sans MS", 30, 'bold'))
    draw_continue_button(150, 0, "No")
    draw_continue_button(-330, 0, "Yes")

def image_color_changer(image_name, turt, duck_or_model, duck_or_model_reference):
    user_duck_image = Image.open(image_name).convert("RGBA")
    reference_image = Image.open(duck_or_model_reference).convert("RGBA")
    for x in range(reference_image.width):      
        for y in range(reference_image.height):
            r,g,b,a = reference_image.getpixel((x,y))

            if (r,g,b) == (255, 255, 255): #look here if errors
                if turt == basic_duck: #red
                    r,g,b = (224,31,31)
                elif turt == flower_duck: #orange
                    r,g,b = (224,88,31)
                elif turt == glasses_duck: #yellow
                    r,g,b = (224,197,31)
                elif turt == heart_duck: #green
                    r,g,b = (46,152,20)
                elif turt == leaf_duck: #blue
                    r,g,b = (22,81,156)
                elif turt == monacle_duck: #pink
                    r,g,b = (236,124,231)
                elif turt == tophat_duck: #violet
                    r,g,b = (160,12,236)
                elif turt == white_color_turtle: #white
                    r,g,b = (255,255,255)
            user_duck_image.putpixel((x,y),(r,g,b,a))
    user_duck_image.save(image_name)
    

    turtle.addshape(image_name)
    shape = image_name
    duck_or_model.shape(shape)
    


def user_duck_choice(x,y):
    if current_loc == 'customization':
        for turt in buttons:
            if turt.distance(x,y) <= 80 and step == 'hats' and turt != white_color_turtle:
                shape = "DucksIconsLarge/"+string_hat_buttons[buttons.index(turt)]+'.gif'
                model_reference = Image.open("model_white_accessory.gif").convert("RGBA")
                current_choice_model = Image.open(shape).convert("RGBA")
                for x in range(model_reference.width):      
                    for y in range(model_reference.height):
                        r,g,b,a = current_choice_model.getpixel((x,y))   
                        model_reference.putpixel((x,y),(r,g,b,a))
                model_reference.save("model_white_accessory.gif")
                turtle.addshape("model_white_accessory.gif")
                model_duck.shape(shape)
                
                
                shape_img_proc = shape.replace('DucksIconsLarge','Ducks')
                shape_img_proc = shape_img_proc.replace('2x','')
                duck.shape(shape_img_proc)
                user_duck_image = Image.open("user_duck.gif").convert("RGBA")
                last_saved_choice_image = Image.open(shape_img_proc).convert("RGBA")


                for x in range(last_saved_choice_image.width):      
                    for y in range(last_saved_choice_image.height):
                        r,g,b,a = last_saved_choice_image.getpixel((x,y))   
                        user_duck_image.putpixel((x,y),(r,g,b,a))
                user_duck_image.save("user_duck.gif")
                last_saved_choice_image.save("white_duck_with_accessory.gif")

            elif turt.distance(x,y) <= 80 and step == 'colors':
                image_color_changer("user_duck.gif", turt, duck, "white_duck_with_accessory.gif")
                image_color_changer("model_duck_scaled.gif", turt, model_duck,"model_white_accessory.gif")
            

def hide_turtles():
    for i in buttons:
        i.hideturtle()
        i.penup()
    white_color_turtle.hideturtle()
def show_turtles():
    for i in buttons[:7]:
        i.showturtle()
        i.penup()
def clear_turtles():
    drawing_turtle.clear()
    writing_turtle.clear()
def setup_buttons(folder,list_name):
    if step == 'hats':
        hide_turtles()
        dx = 0
        for turt in buttons[0:3]:
            shape = folder+list_name[buttons.index(turt)]+'.gif'
            turt.shape(shape)
            turt.goto(175+dx,50)
            dx += 150
        dx = 0
        for turt in buttons[3:7]:
            shape = folder+list_name[buttons.index(turt)]+'.gif'
            turt.shape(shape)
            turt.goto(100+dx,-100)
            dx += 150
    elif step == 'colors':
        hide_turtles()
        dx = 0
        for turt in buttons[0:3]:
            shape = folder+list_name[buttons.index(turt)]+'.gif'
            turt.shape(shape)
            turt.goto(100+dx,50)
            dx += 150
        dx = 0
        for turt in buttons[3:7]:
            shape = folder+list_name[buttons.index(turt)]+'.gif'
            turt.shape(shape)
            turt.goto(100+dx,-100)
            dx += 150
        shape = "Colors/WHITE.gif"
        white_color_turtle.shape(shape)
        white_color_turtle.goto(550, 50)
        white_color_turtle.showturtle()
    for turt in buttons:
        turt.onclick(user_duck_choice)  #could be a source of problems (for loop as well)
    show_turtles()
    s.update()


#Functionality Turtles
turtle.hideturtle()

model_duck = turtle.Turtle()
model_duck.hideturtle()
model_duck.penup()
model_duck.shape("DucksIconsLarge/basic_duck2x.gif")




def enter_character_custom():
    global step

    if current_loc == 'customization':
        step = 'introduction'
        duck.hideturtle()
        s.bgpic('Scenes/royalblue.gif')
        writing_turtle.goto(0,0)
        writing_turtle.write("Welcome to the character customization!", False, align="center", font=("Comic Sans MS", 30, 'bold'))
        draw_continue_button(-60, -20, "Continue")
        
        
        #Setup for image consistency
        user_duck_image_small = Image.open("Ducks/basic_duck.gif").convert("RGBA")
        user_duck_image_large = Image.open("DucksIconsLarge/basic_duck2x.gif").convert("RGBA")
        
        user_duck_image_small.save("user_duck.gif")
        user_duck_image_small.save("white_duck_with_accessory.gif")
        user_duck_image_large.save("model_duck_scaled.gif")
        user_duck_image_large.save("model_white_accessory.gif")

        turtle.addshape("model_duck_scaled.gif")
        turtle.addshape("user_duck.gif")
        model_duck.shape("model_duck_scaled.gif")
        duck.shape("user_duck.gif")

    
hide_turtles()
s.onclick(location_of_click)

# s.mainloop()
# turtle.done()
################################# END OF CHAR CUSTOM ############################################################
def play_game():
    while gameStatus:
        s.onkey(move_up, "Up")
        s.onkey(move_down, "Down")
        s.onkey(move_left, "Left")
        s.onkey(move_right, "Right")
        s.onkey(exit_game, "Escape")
        #s.update() #alternate solution if s.mainloop() makes things weird

        s.listen()
        s.mainloop()
    

########## MAIN ##########
game_setup()
play_game()



