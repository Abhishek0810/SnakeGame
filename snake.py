import pygame #to  import the pygame module
import random   #random.ran int function can be initiated for the snake food.
import os           #to create a file

#This is for to play music in background
#pygame.mixer.init()
#pygame.mixer.music.load('abc.mp3')
#pygane.mixer.music.play()

pygame.init()  #to initialize the pygame module



# Colors(Defining colors for the windows
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green=(0,255,0)
# Creating window

gameWindow = pygame.display.set_mode((700,650))


#background image
#bgimg=pygame.image.load("abc.jpg")
#bgimg=pygame.transform.scale(bgimg,(700,650)).convert_alpha()


# Game Title(TO display the title of the window)
pygame.display.set_caption("My sapoli game")
pygame.display.update()
clock = pygame.time.Clock()            #using clock for moving or frame per sect
font = pygame.font.SysFont(None, 55)   #giving the size of the font



#This fucntion diplay color onscreen
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

#This function plot the rectngle for the snake body
def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:           #loop for the list to enlarge snake
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(green)
        text_screen("Lets get start",black,150,250)
        text_screen("press spacebar to play",black,10,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()


        pygame.display.update()
        clock.tick(60)






# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False             #conditional varables if it true user will exit the game
    game_over = False
    snake_x = 45                 #inital postion of snake along x-xis
    snake_y = 55
    velocity_x = 0         #this variable is for to provide veloctiy to out snake
    velocity_y = 0
    snake_list = []
    snake_length = 1

    #for creating highscore file when our highscore file is deleted
    if(not os.path.exists("Highscore.txt")):
        with open("Highscore.txt","w") as f:
            f.write("0")


    #this is for to read the high score in the game
    with open("highscore.txt", "r") as f:
        highscore = f.read()

    food_x = random.randint(20, 500 / 2)              #food position for the snake along x-axis
    food_y = random.randint(20,650 / 2)
    score = 0
    init_velocity = 5
    snake_size = 30
    size=30
    fps = 60

    #creating a game loop
    while not exit_game:
       #game over display onscreen
        if game_over:
            #this function write the high score highscore.txt file.
            with open("highscore.txt", "w") as f:

                f.write(str(highscore))

            gameWindow.fill(black)
            #gameWindow.blit(bgimg,(0,0))  #to diplay BG image
            text_screen("bBtt", red, 10, 300) #

            for event in pygame.event.get():      #performing event
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:#For restart the game
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0                #if it is having some velocity for x then accordingly velocity for y is 0.

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    #cheat for game..
                    #if event.key==pygame.K_q:
                        #score=score+15

            # giving the velocity to our snake.usko move karana hai jab ek tap mein to...
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            # abs stands for absolute value
            # this function we make and update our scores for food
            if abs(snake_x - food_x)<20 and abs(snake_y - food_y)<20:
                score = score+10
                food_x = random.randint(20, 800 / 2)
                food_y = random.randint(20, 600 / 2)
                snake_length =snake_size+5

                #high score condition:
            if score>int(highscore):
                highscore=score
            gameWindow.fill(black)
            text_screen("Score: " + str(score) +"      High Score:" +str(highscore), red, 5, 5) #prnting highescore in screen as well as other part.
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, size])


            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            # this check the whether the snake length is less than the snake size.
            if len(snake_list)>(snake_length):
                del snake_list[0]
                # pygame.draw.rect(gameWindow, green, [food_x, food_y, snake_size, size])

            #It is used if our snake head touches our body game will be over
            if head in snake_list[:-1]:
                game_over = True

               #It is used for if our snake touch screen from given parameter game will be over
            if snake_x<0 or snake_x>800 or snake_y<0 or snake_y>600:
                game_over = True
            # for to increase the snake size and length
            plot_snake(gameWindow, green, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
    #gameloop()
welcome()
