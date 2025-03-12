import pygame

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 7
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Paddle and Ball Properties
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
paddle1 = pygame.Rect(20, HEIGHT//2 - 60, 10, 120)
paddle2 = pygame.Rect(WIDTH - 30, HEIGHT//2 - 60, 10, 120)
ball_speed_x = BALL_SPEED
ball_speed_y = BALL_SPEED
paddle1_speed = 0
paddle2_speed = 0

# Game Loop
running = True
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Paddle Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_speed = -PADDLE_SPEED
            if event.key == pygame.K_s:
                paddle1_speed = PADDLE_SPEED
            if event.key == pygame.K_UP:
                paddle2_speed = -PADDLE_SPEED
            if event.key == pygame.K_DOWN:
                paddle2_speed = PADDLE_SPEED
        
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_w, pygame.K_s):
                paddle1_speed = 0
            if event.key in (pygame.K_UP, pygame.K_DOWN):
                paddle2_speed = 0
    
    # Move paddles
    paddle1.y += paddle1_speed
    paddle2.y += paddle2_speed
    
    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1
    
    # Ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed_x *= -1
    
    # Ball goes out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x, ball.y = WIDTH//2 - 15, HEIGHT//2 - 15
        ball_speed_x *= -1
    
    # Draw elements
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))
    
    # Update display
    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
