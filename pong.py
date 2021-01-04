import pgzrun
colour=(24,11,7)
WIDTH = 1000
HEIGHT =500
ball = Actor('ball')
ball_x_speed = 5
ball_y_speed =1
paddle = Actor('paddle')
paddle.pos = 200, 470
mark=0
missed = False

def draw():
    screen.fill(colour)
    ball.draw()
    paddle.draw()
    draw_text()
    screen.draw.text("score :"+str(mark),(10,0),fontsize =40,color="white")

def update():
    if not missed:
       animate_ball()
    

def on_mouse_move(pos):
    
    paddle.x=pos[0]
    if paddle.left<0:
        paddle.left=0
    if paddle.right>WIDTH:
         paddle.right =WIDTH

def animate_ball():
    ball.x+= ball_x_speed
    ball.y+= ball_y_speed
    check_boundary()
    check_collision()
    check_paddle_miss()

def check_collision():
    global ball_y_speed ,score,mark
    if ball.colliderect(paddle):
        ball_y_speed*=-1
        mark+=1
   

def check_boundary():
    global ball_x_speed, ball_y_speed
    if ball.right >WIDTH or ball.left <0:
       ball_x_speed *=-1
    
    if ball.top < 0 or ball.bottom >HEIGHT :
        ball_y_speed *=-1

def check_paddle_miss():
    global missed
    if ball.bottom > paddle.top+ abs(ball_y_speed):
        missed=True

def draw_text():
    if missed:
        screen.draw.text("oops missed",(200,20),fontsize =40,color="red")
pgzrun.go()

