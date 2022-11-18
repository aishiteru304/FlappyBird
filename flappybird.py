import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((400,600))
pygame.display.set_caption('Flappy Bird')
clock=pygame.time.Clock()
WHITE=(255,255,255)
RED=(255,0,0)
x_bird=50
y_bird=150
x_pipe1=400
x_pipe2=600
x_pipe3=800
y_pipe1=0
y_pipe2=0
y_pipe3=0
width_pipe=50
height_pipe1=randint(100,400)
height_pipe2=randint(100,400)
height_pipe3=randint(100,400)
gap_pipe=150
pipe_speed=2
bird_speed=0
pipe1_pass=0
pipe2_pass=0
pipe3_pass=0
score=0
pause=0

font=pygame.font.SysFont('san',20)
fontover=pygame.font.SysFont('san',50)
background_img=pygame.image.load('images/background.png')
background_img=pygame.transform.scale(background_img,(400,600))
bird_img=pygame.image.load('images/bird.png')
bird_img=pygame.transform.scale(bird_img,(35,35))
pipe_img=pygame.image.load('images/pipe.png')
pipe_op_img=pygame.image.load('images/pipe_op.png')
sand_img=pygame.image.load('images/sand.png')
sand_img=pygame.transform.scale(sand_img,(400,30))
running=True
while running:
    clock.tick(60)
    screen.fill(WHITE)
    screen.blit(background_img,(0,0))
    

    #Draw pipe
    pipe1_img=pygame.transform.scale(pipe_img,(width_pipe,height_pipe1))
    pipe1=screen.blit(pipe1_img,(x_pipe1,y_pipe1))
    pipe2_img=pygame.transform.scale(pipe_img,(width_pipe,height_pipe2))
    pipe2=screen.blit(pipe2_img,(x_pipe2,y_pipe2))
    pipe3_img=pygame.transform.scale(pipe_img,(width_pipe,height_pipe3))
    pipe3=screen.blit(pipe3_img,(x_pipe3,y_pipe3))

    #Draw pipe opposite
    pipe1_op_img=pygame.transform.scale(pipe_op_img,(width_pipe,600-gap_pipe-height_pipe1))
    pipe_op1=screen.blit(pipe1_op_img,(x_pipe1,gap_pipe+height_pipe1))
    pipe2_op_img=pygame.transform.scale(pipe_op_img,(width_pipe,600-gap_pipe-height_pipe2))
    pipe_op2=screen.blit(pipe2_op_img,(x_pipe2,gap_pipe+height_pipe2))
    pipe3_op_img=pygame.transform.scale(pipe_op_img,(width_pipe,600-gap_pipe-height_pipe3))
    pipe_op3=screen.blit(pipe3_op_img,(x_pipe3,gap_pipe+height_pipe3))

    #Draw pipe to left 
    x_pipe1-=pipe_speed
    x_pipe2-=pipe_speed
    x_pipe3-=pipe_speed

    #Write score
    string_score=font.render("Score: "+str(score),True,RED)
    screen.blit(string_score,(5,5))
    if( x_bird > x_pipe1 + width_pipe and pipe1_pass==0 ):
            score+=1 
            pipe1_pass=1
    if( x_bird > x_pipe2 + width_pipe and pipe2_pass==0 ):
            score+=1 
            pipe2_pass=1
    if( x_bird > x_pipe3 + width_pipe and pipe3_pass==0 ):
            score+=1 
            pipe3_pass=1
        
    #Create new pipe
    if(x_pipe1<-width_pipe):
        x_pipe1=x_pipe3+200
        height_pipe1=randint(100,400)
        pipe1_pass=0
    if(x_pipe2<-width_pipe):
        x_pipe2=x_pipe1+200
        height_pipe2=randint(100,400)
        pipe2_pass=0
    if(x_pipe3<-width_pipe):
        x_pipe3=x_pipe2+200
        height_pipe3=randint(100,400)
        pipe3_pass=0

    #Draw sand
    sand=screen.blit(sand_img,(0,570))
    #Draw bird 
    bird=screen.blit(bird_img,(x_bird,y_bird))
    y_bird+=bird_speed
    bird_speed+=0.5

    #Collision bird & pipe
    pipes=[pipe1,pipe2,pipe3,pipe_op1,pipe_op2,pipe_op3,sand]
    for pipe in pipes:
        if bird.colliderect(pipe):
            gameover=fontover.render("Game over!!! ",True,RED)
            screen.blit(gameover,(100,300))
            pipe_speed=0
            bird_speed=0
            pause=1

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                bird_speed=-7
                if(pause):
                    x_bird=50
                    y_bird=150
                    x_pipe1=400
                    x_pipe2=600
                    x_pipe3=800
                    score=0
                    pipe_speed=2
                    bird_speed=0
                    pause=0

    pygame.display.flip()
pygame.quit()
