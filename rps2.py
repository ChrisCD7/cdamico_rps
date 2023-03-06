# import libraries

from time import sleep

from random import randint 

import pygame as pg

import os

game_folder = os.path.dirname(__file__)
print(game_folder)

# game settings
WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
# tuples are immutable - cannot change once created
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

choices = ["rock", "paper", "scissors"]

def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)

def cpu_randchoice():
    choice = choices[randint(0,2)]
    print("computer randomly decides..." + choice)
    return choice

pg.init()
pg.mixer.init()

screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Rock, Paper, Scissors...")
clock = pg.time.Clock()

phil_image = pg.image.load(os.path.join(game_folder, 'drphil1.jpg')).convert()
phil_rect = phil_image.get_rect()
cpu_phil_rect = phil_image.get_rect()

paper_image = pg.image.load(os.path.join(game_folder, 'paper.jpg')).convert()
paper_image_rect = paper_image.get_rect()
cpu_paper_rect = paper_image.get_rect()

scissors_image = pg.image.load(os.path.join(game_folder, 'scissors.jpg')).convert()
scissors_image_rect = scissors_image.get_rect()
cpu_sciss_rect = scissors_image.get_rect()

start_screen = True

player_choice = ""
cpu_choice = ""
running = True

while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # ########## input ###########
        # HCI - human computer interaction...
        # keyboard, mouse, controller, vr headset
        # checks for keyboard
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                print("game on!!!!")
                start_screen = False
        
        if event.type == pg.MOUSEBUTTONUP:
            # 
            print(pg.mouse.get_pos()[0])
            # 
            print(pg.mouse.get_pos()[1])
            # 
            mouse_coords = pg.mouse.get_pos()

            print(phil_rect.collidepoint(mouse_coords))
            if phil_rect.collidepoint(mouse_coords):
                print("you clicked on rock..")
                player_choice = "rock"
                cpu_choice = cpu_randchoice()
                # call a function that gets the cpu choice...
            elif paper_image_rect.collidepoint(mouse_coords):
                print("you clicked on paper...")
                player_choice = "paper"
                cpu_choice = cpu_randchoice()
       
            elif scissors_image_rect.collidepoint(mouse_coords):
                print("you clicked on scissors...")
                player_choice = "scissors"
                cpu_choice = cpu_randchoice()                      
            else:
                print("you didn't click on anything...")
    
    
    

    ############ draw ###################
    screen.fill(WHITE)

    # waits for player to hit space bar
    if start_screen == True:
        draw_text("Click Space to Continue", 22, RED, WIDTH/2, HEIGHT/10)
        phil_rect.x = 2000
        paper_image_rect.x = 2000
        scissors_image_rect.x = 2000

    # allows player to choose rock paper or scissors
    if not start_screen and player_choice == "":
        phil_rect.x = 50
        paper_image_rect.x = 350
        scissors_image_rect.x = 550
        screen.blit(scissors_image, scissors_image_rect)
        screen.blit(paper_image, paper_image_rect)
        screen.blit(phil_image, phil_rect)

    # compare
    if player_choice == "rock":
        if cpu_choice == "rock":
            cpu_phil_rect.x = 500
            screen.blit(phil_image, phil_rect)
            screen.blit(phil_image, cpu_phil_rect)
            draw_text("DRAW!!!", 22, RED, WIDTH/2, HEIGHT/10)
    elif player_choice == "rock":
        if cpu_choice == "paper":
            cpu_paper_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_rect)
            draw_text("You LOSE AHAHA!", 22, RED, WIDTH/2, HEIGHT/10)
    elif player_choice == "rock":
        if cpu_choice == "scissors":
            cpu_sciss_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_sciss_rect)
            draw_text("ahh you won", 22, RED, WIDTH/2, HEIGHT/10)
    elif player_choice == "paper":
        if cpu_choice == "paper":
            cpu_paper_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_rect)
            draw_text("DRAW!", 22, RED, WIDTH/2, HEIGHT/10)
    elif player_choice == "paper":
        if cpu_choice == "rock":
            cpu_phil_rect.x = 500
            screen.blit(phil_image, phil_rect)
            screen.blit(phil_image, cpu_phil_rect)
            draw_text("ah..man you won.", 22, RED, WIDTH/2, HEIGHT/10)
    elif player_choice == "paper":
        if cpu_choice == "scissors":
            cpu_sciss_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_rect)
            draw_text("haha you lose!", 22, RED, WIDTH/2, HEIGHT/10)
    elif player_choice == "scissors":
        if cpu_choice == "scissors":
            cpu_sciss_rect.x = 500
            screen.blit(scissors_image, scissors_image_rect)
            screen.blit(scissors_image, cpu_sciss_rect)
            draw_text("DRAW!!", 22, RED, WIDTH/2, HEIGHT/10)
    elif player_choice == "scissors":
        if cpu_choice == "rock":
            cpu_phil_rect.x = 500
            screen.blit(phil_image, phil_rect)
            screen.blit(phil_image, cpu_phil_rect)
            draw_text("HAHA you lose!!", 22, RED, WIDTH/2, HEIGHT/10)
    elif player_choice == "scissors":
        if cpu_choice == "paper":
            cpu_paper_rect.x = 500
            screen.blit(paper_image, paper_image_rect)
            screen.blit(paper_image, cpu_paper_rect)
            draw_text("you..win..", 22, RED, WIDTH/2, HEIGHT/10)


    pg.display.flip()

pg.quit()