background = codesters.Rectangle(0,0,500,500,"darkgray") # darkGrey background
red_goal = codesters.Rectangle(0,240,100,22,"red") # Red goal
blue_goal = codesters.Rectangle(0,-240,100,22,"blue") # Blue goal
board = codesters.Rectangle(0,0,300,460,"white") # White playing area

p1 = codesters.Circle(0,150,30,"red") # Player 1 (red circle)
p2 = codesters.Circle(0,-150,30,"blue") # Player 2 (blue circle)

puck = codesters.Circle(0,0,20,"black") # Black puck
puck.set_y_speed(random.choice([-5,5])) # Set puck speed in Y direction
puck.set_x_speed(random.randint(-4,4)) # Set puck speed in X direction

blue_score = 0 # Score for blue team
red_score = 0 # Score for red team
blue_display = codesters.Text("Blue:\n0",200,200,"blue") # Display score for blue team
red_display = codesters.Text("Red:\n0",-200,200,"red") # Display score for red team

# Controls for Player 1
def p1_up():
    if p1.get_top() < 230:
        p1.move_up(15) # Move Player 1 up
stage.event_key("w",p1_up)

def p1_down():
    if p1.get_bottom() > 20:
        p1.move_down(15) # Move Player 1 down
stage.event_key("s",p1_down)

def p1_left():
    if p1.get_left() > -150:
        p1.move_left(15) # Move Player 1 left
stage.event_key("a",p1_left)

def p1_right():
    if p1.get_right() < 150:
        p1.move_right(15) # Move Player 1 right
stage.event_key("d",p1_right)

# Controls for Player 2
def p2_up():
    if p2.get_top() < -20:
        p2.move_up(15) # Move Player 2 up
stage.event_key("up",p2_up)

def p2_down():
    if p2.get_bottom() > -230:
        p2.move_down(15) # Move Player 2 down
stage.event_key("down",p2_down)

def p2_left():
    if p2.get_left() > -150:
        p2.move_left(15) # Move Player 2 left
stage.event_key("left",p2_left)

def p2_right():
    if p2.get_right() < 150:
        p2.move_right(15) # Move Player 2 right
stage.event_key("right",p2_right)

def reset():
    blue_display.set_text("Blue:\n{}".format(blue_score)) # Update score for blue team
    red_display.set_text("Red:\n{}".format(red_score)) # Update score for red team
    puck.go_to(0,0) # Move puck back to the middle
    puck.set_y_speed(0) # Stop puck movement in Y direction
    puck.set_x_speed(0) # Stop puck movement in X direction
    if red_score >= 7:
        codesters.Text("Red Wins",0,0,"red") # Show "Red Wins" message
        puck.hide() # Hide the puck
    elif blue_score >= 7:
        codesters.Text("Blue Wins",0,0,"blue") # Show "Blue Wins" message
        puck.hide() # Hide the puck
    else:
        stage.wait(2) # Wait for 2 seconds
        puck.set_y_speed(random.choice([-5,5])) # Set new Y direction speed for puck
        puck.set_x_speed(random.randint(-4,4)) # Set new X direction speed for puck

# Event when puck collides with something
def puck_collision(puck,hit_sprite):
    global red_score, blue_score
    # Handle collision with the edges
    if hit_sprite is background:
        if puck.get_left() < -150:
            puck.set_left(-150) # Keep puck from going too far left
            puck.set_x_speed(puck.get_x_speed()*-1) # Bounce puck back to the right
        elif puck.get_right() > 150:
            puck.set_right(150) # Keep puck from going too far right
            puck.set_x_speed(puck.get_x_speed()*-1) # Bounce puck back to the left
        if puck.get_top() > 230:
            puck.set_top(230) # Keep puck from going too far up
            puck.set_y_speed(puck.get_y_speed()*-1) # Bounce puck back down
        elif puck.get_bottom() < -230:
            puck.set_bottom(-230) # Keep puck from going too far down
            puck.set_y_speed(puck.get_y_speed()*-1) # Bounce puck back up
    # Handle collision with players
    elif hit_sprite is p1 or hit_sprite is p2:
        if puck.get_x_speed() > 0:
            if puck.get_x() > hit_sprite.get_x():
                puck.set_x_speed(puck.get_x_speed()+1) # Make puck go faster in X direction
            else:
                puck.set_x_speed((puck.get_x_speed()-1)*-1) # Reverse and slow down puck in X direction
        else:
            if puck.get_x() > hit_sprite.get_x():
                puck.set_x_speed((puck.get_x_speed()-1)*-1) # Reverse and slow down puck in X direction
            else:
                puck.set_x_speed(puck.get_x_speed()-1) # Slow down puck in X direction
        if puck.get_y_speed() > 0:
            if puck.get_y() < hit_sprite.get_y():
                puck.set_y_speed(puck.get_y_speed()*-1) # Reverse puck direction in Y
        else:
            if puck.get_y() > hit_sprite.get_y():
                puck.set_y_speed(puck.get_y_speed()*-1) # Reverse puck direction in Y
    # Check if puck hits red goal
    elif hit_sprite is red_goal:
        blue_score += 1 # Add point to blue team
        reset() # Reset the game
    # Check if puck hits blue goal
    elif hit_sprite is blue_goal:
        red_score += 1 # Add point to red team
        reset() # Reset the game
puck.event_collision(puck_collision) # Collision event for the puck



