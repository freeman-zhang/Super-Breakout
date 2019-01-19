# I - IMPORT AND INITIALIZE
import pygame, PongSprites
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((640, 480))
 

     
def main():
    '''This function defines the 'mainline logic' for our pyPong game.'''
      
    # DISPLAY
    pygame.display.set_caption("pyPong! v2.0")
     
    # ENTITIES
    
    # Create a list of Joystick objects.
    joysticks = []
    for joystick_no in range(pygame.joystick.get_count()):
        stick = pygame.joystick.Joystick(joystick_no)
        stick.init()
        joysticks.append(stick)    
    
    background = pygame.image.load('background.png')
    background = background.convert()
    screen.blit(background, (0, 0))
    
    #background music
    pygame.mixer.music.load('background.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.3)
    #sound effects
    bounce = pygame.mixer.Sound('bounce.wav')
    bounce.set_volume(0.5)
    score = pygame.mixer.Sound('score.wav')
    score.set_volume(0.6)
    
    # Sprites for: ScoreKeeper label, End Zones, Ball, and Players
    score_keeper = PongSprites.ScoreKeeper()
    ball = PongSprites.Ball(screen)
    player1 = PongSprites.Player(screen, 1)
    player1_endzone = PongSprites.EndZone(screen,0)
    player2 = PongSprites.Player(screen, 2)
    player2_endzone = PongSprites.EndZone(screen,639)
    allSprites = pygame.sprite.Group(score_keeper, player1_endzone, \
                                     player2_endzone, ball, player1, player2)
    
    # ASSIGN 
    clock = pygame.time.Clock()
    keepGoing = True
 
    # Hide the mouse pointer
    pygame.mouse.set_visible(False)
 
    # LOOP
    while keepGoing:
     
        # TIME
        clock.tick(30)
     
        # EVENT HANDLING: Player 1 uses joystick, Player 2 uses arrow keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False

                '''
            elif event.type == pygame.JOYHATMOTION:
                player1.change_direction(event.value)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player2.change_direction((0, 1))
                if event.key == pygame.K_DOWN:
                    player2.change_direction((0, -1))
                '''
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1.change_direction((0, 1))
                if event.key == pygame.K_s:
                    player1.change_direction((0, -1))

                if event.key == pygame.K_UP:
                    player2.change_direction((0, 1))
                if event.key == pygame.K_DOWN:
                    player2.change_direction((0, -1))
                    
        
 
        # Check if player 1 scores (i.e., ball hits player 2 endzone)
        if ball.rect.colliderect(player2_endzone):
            score_keeper.player1_scored()
            ball.change_direction()
            score.play(0)
 
        # Check if player 2 scores (i.e., ball hits player 1 endzone)
        if ball.rect.colliderect(player1_endzone):
            score_keeper.player2_scored()
            ball.change_direction()
            score.play(0)
            
        # Check for game over (if a player gets 3 points)
        if score_keeper.winner():
            keepGoing = False
           
                     
        # Check if ball hits Player 1 or 2
        # If so, change direction, and speed up the ball a little
        if ball.rect.colliderect(player1.rect) or ball.rect.colliderect(player2.rect):
            ball.change_direction()
            ball.increase_speed()
            player1.increase_speed()
            player2.increase_speed()
            bounce.play(0)
                     
        # REFRESH SCREEN
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)       
        pygame.display.flip()
        
    """
    game_over = pygame.Surface(screen.get_size())
    game_over = game_over.convert()
    font = pygame.font.Font("Font.ttf", 50)
    game_over_message = "GAME OVER"
    game_over_label = font.render(game_over_message, 1, (0,0,0))

    screen.blit(game_over_label, (320, 240))
    """     
    
    # Unhide the mouse pointer
    pygame.mouse.set_visible(True)
    
    # Close the game window
    pygame.quit()     
     
# Call the main function
main()    