import pygame
from sys import exit
from random import randint
#set time in game
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surface = font.render(f"Score:{current_time}",False,(204,247,255))
    score_rect = score_surface.get_rect(center=(300,50))
    screen.blit(score_surface,score_rect)
    return current_time
 #create enemy movement list
def enemy_movement(enemy_list):
    if enemy_list:
        for enemy_rect in enemy_list:
            enemy_rect.x -= 6
            # dispaly enemy movement
            screen.blit(snail_surface,enemy_rect)    
        enemy_list = [enemy for enemy in enemy_list if enemy.x > 0]
 
        return enemy_list
    else: return []
    #collision between player and enemy
def collision(player,enemy):
    if enemy:
        for enemy_rect in enemy:
            if player.colliderect(enemy_rect):return False
    return True
def player_animation():
    global player_Naruto,player_index
    #walking animation # jump surface
    if player_rect.bottom < 525:
        player_Naruto = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_Naruto = player_walk[int(player_index)]
# general setup
pygame.init()
#create the display surface
screen = pygame.display.set_mode((600,600))

#updating the display
pygame.display.set_caption("runner")  
clock = pygame.time.Clock()
font = pygame.font.Font(None, 50)
game_active = False
start_time = 0
score = 0

#updating the surface by importing picture
town_surface = pygame.image.load("s.pygame.jpg").convert()
background = pygame.transform.smoothscale(town_surface, screen.get_size())
ground_surface = pygame.image.load("g.pygame.png").convert_alpha()

#score_surface = font.render("runner", False,(204,247,255)) 
#score_rect = score_surface.get_rect(center=(300,50))
#load image
#enemy image
snail_frame_1 = pygame.image.load("no.pygame.png").convert_alpha()
snail_frame_1 = pygame.transform.smoothscale(snail_frame_1,screen.get_size())
snail_frame_1 = pygame.transform.scale(snail_frame_1, (35, 35))
snail_frame_2 = pygame.image.load("no.pygame.png").convert_alpha()
snail_frame_2 = pygame.transform.smoothscale(snail_frame_2,screen.get_size())
snail_frame_2 = pygame.transform.scale(snail_frame_2, (35, 35))
snail_frames = [snail_frame_1,snail_frame_2]
snail_index = 0
snail_surface = snail_frames[snail_index]
snail_rect = snail_surface.get_rect(midright = (600,500))
#create obstacle list
enemy_rect_list = []

# Load the player image and set its initial position
player_walk_1 = pygame.image.load("n.pygame.png").convert_alpha()
player_walk_1 = pygame.transform.scale(player_walk_1,(50,50)) 
player_walk_2 = pygame.image.load("n.pygame.png").convert_alpha()
player_walk_2 = pygame.transform.scale(player_walk_2,(25,25))
player_walk = [player_walk_1,player_walk_2]
player_index = 0
player_jump = pygame.image.load("jump.pygame.png").convert_alpha()
player_jump = pygame.transform.scale(player_jump,(25,25))
player_Naruto = player_walk[player_index]
player_rect = player_Naruto.get_rect(midbottom = (80,525))
Naruto_gravity = -15
#add intro screen
Naruto_stand = pygame.image.load("op.pygame.jpg").convert_alpha()
Naruto_stand = pygame.transform.smoothscale(Naruto_stand,screen.get_size())
Naruto_stand = pygame.transform.scale(Naruto_stand,(50,50))
Naruto_rect = Naruto_stand.get_rect(center = (300,300))

#add title for game
game_title = font.render("Naruto",False,(93,138,168))
game_title_rect = game_title.get_rect(center = (300,250))

# add obstacle timer
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer,1500)
# timer for snail
snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)


# everything is going to run through while true loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #mouse position
        if game_active:
           if event.type == pygame.MOUSEBUTTONDOWN:
              if player_rect.Collidepoint(event.pos) and player_rect.bottom >= 52:
                 Naruto_gravity = -15
           if event.type == pygame.KEYDOWN and player_rect.bottom >= 525:
               if event.key == pygame.K_SPACE:
                  Naruto_gravity = -15
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 600
                start_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            if event.type == enemy_timer and game_active:
                enemy_rect_list.append(snail_surface.get_rect(midright =(randint(900,1000),500))) 
            
       # for updating timers
            if event.type == snail_animation_timer:
                if snail_index == 0: snail_index = 1
                else: snail_index = 0
                snail_surface = snail_frames[snail_index] 
           
                
    if game_active:   
      #crating the background        
        screen.blit(background,(0,0))
        screen.blit(ground_surface,(0,500))
        score = display_score()
    
        #add player gravity
        Naruto_gravity += 1
        player_rect.y += Naruto_gravity
        if player_rect.bottom >= 525:
           player_rect.bottom = 525
        player_animation()
        screen.blit(player_Naruto,player_rect)
        #obstacle movement
        enemy_rect_list = enemy_movement(enemy_rect_list)
        
        #colllision
        game_active = collision(player_rect,enemy_rect_list)
    
    else:
        screen.fill((63,191,191))
        screen.blit(Naruto_stand,Naruto_rect) 
        enemy_rect_list.clear()
        player_rect.midbottom = (80,525)
        Naruto_gravity = 0
        score_message = font.render(f"your score:{score}",False,(93,138,168))
        score_message_rect = score_message.get_rect(center = (300,250))
        #display score message
        if score == 0:
           screen.blit(game_title,game_title_rect)
        else:
            screen.blit(score_message,score_message_rect)
        
            
    pygame.display.update()
    clock.tick(60)