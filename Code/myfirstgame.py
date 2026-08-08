import pygame
import time
import random
import button
pygame.init()
pygame.font.init()
pygame.mixer.init()


boopi = pygame.mixer.Sound("UI/boop.wav") 
hu = pygame.mixer.Sound("UI/Huh!.wav")

    


WIDTH,HEIGHT = 1400,795
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("DODGE THE METEORS")


STAR_VELOCITY = 0
PLAYER_VEL = 20
meteor = pygame.transform.scale(pygame.image.load("UI/meteor.png"), (30,40))
player_WIDTH = 40
player_HEIGHT= 60
STAR_WIDTH = 20
STAR_HEIGHT = 20
FONT = pygame.font.Font("UI/G7.ttf", 30)
fonti = pygame.font.Font("UI/G7.ttf", 15)

I = ["UI/goodbg.jpg","UI/Beta.jpg"]

black = (0,0,0)
file=random.choice(I) 

def draw(player, elapsed_time, stars): 
 #   WIN.fill(black)
  

#96, 130, 182
    time_text = FONT.render(f"{round(elapsed_time)}s",1,'white')
    WIN.blit(time_text,(650,10))
    pygame.draw.rect(WIN,"white", player)
    
    pause_text = FONT.render("PRESS SPACE TO PAUSE ", 1, "green")
    WIN.blit(pause_text,(400,50))
    tell_text = fonti.render("RIGHT - D / RIGHT ARROW | LEFT - A OR LEFT ARROW", 1, 'white')
    WIN.blit(tell_text, (400,80))
    
    for star in stars:
         WIN.blit(meteor, star)

    
    colour = ["red", "blue", "green","purple", "white","pink"]
    for i in colour:
            i = random.choice(colour)
            pygame.draw.rect(WIN, i, player)
 
    pygame.display.update()



def main():
    run = True
    hi_time = 0 
    player = pygame.Rect(200,HEIGHT-player_HEIGHT, player_WIDTH, player_HEIGHT) 
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    easy = False
    med = False
    hard = False
    star_add_increment = 0
    star_count = 0

    draws = True
    stars = []
    HIT = False
    tries = True
    while run:
        
        if tries == True:
            draws = False
            WIN.fill("black")
            file = random.choice(I) 

            pygame.display.set_caption("MAIN-MENU")

            MENU_TEXT = FONT.render("MAIN MENU", True, "white")
            WIN.blit(MENU_TEXT, (560,150))

            ezy_img = pygame.image.load("UI/easy_btn.png").convert_alpha()
            ezy_button = button.Button(400,330, ezy_img, 1)

            start_img = pygame.image.load("UI/start_btn.png").convert_alpha()
            start_button = button.Button(560,300, start_img, 1)

            quit_img = pygame.image.load("UI/exit_btn.png").convert_alpha()
            quit_button = button.Button(580,500, quit_img, 1)    

            hard_img = pygame.transform.scale(pygame.image.load("UI/hard_btn.png"), (247,126)).convert_alpha()
            hard_button = button.Button(770, 330, hard_img, 1)

            if start_button.draw(WIN):
                WIN.fill("black")
                if ezy_button.draw(WIN):
                    easy = True
                    if easy == True:
                        STAR_VELOCITY =10
                        PLAYER_VEL = 10
                    draws = True
                    tries = False

                elif hard_button.draw(WIN):
                    hard = True
                    if hard == True:
                        STAR_VELOCITY =15
                        PLAYER_VEL = 12

                    draws = True
                    tries = False
                    pygame.time.delay(100)

            elif quit_button.draw(WIN):
                break 
            pygame.display.update()
        
        
        
        
    
        
        for event in pygame.event.get():
            #pygame.display.set_mode((0,0), pygame.FULLSCREEN)   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_pause = True
            if event.type == pygame.QUIT:
                run = False
                break
                

        if draws:                
            BG = pygame.transform.scale(pygame.image.load(file), (WIDTH,HEIGHT))
            WIN.blit(BG, (0,0))
            star_count += clock.tick(80)
            elapsed_time = time.time() - start_time
            
            if star_count > star_add_increment:
                for _ in range((random.randint(2,3))):
                    star_x = random.randint(0,WIDTH - STAR_WIDTH)
                    star = pygame.Rect(star_x,  STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                    stars.append(star)
            
                star_add_increment = max(300, star_add_increment-100)
                star_count=0
        
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] or keys[pygame.K_LEFT] and player.x - PLAYER_VEL>=0:
                player.x-= PLAYER_VEL
            if keys[pygame.K_d] or keys[pygame.K_RIGHT] and player.x + PLAYER_VEL+ player.width <=WIDTH:
                player.x += PLAYER_VEL
                

            for star in stars[:]:
                star.y += STAR_VELOCITY
                if star.y > HEIGHT:
                    stars.remove(star)
                elif star.y + star.height >= player.y and star.colliderect(player):
                    stars.remove(star)
                    HIT = True
                    break

            if HIT:
                game_pause = True
                boopi.play()
                WIN.fill("black")
                pygame.mixer.music.pause()
                go_text = FONT.render("YOU LOST!", 1, "red")
                WIN.blit(go_text, (WIDTH/2 - go_text.get_width()/2, HEIGHT/2 - go_text.get_height()/2))
                pygame.time.delay(600)
                pygame.display.update()
                hu.play()          
                pygame.display.update()
                pygame.time.delay(3000)

                main()


            draw(player, elapsed_time, stars)        

    pygame.quit()
if __name__ == "__main__":
    main()