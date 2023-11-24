import pygame
import sys
from datetime import datetime

pygame.init()

width, height = 1000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mickey Clock")

clock_face = pygame.image.load("main-clock.png")
m_hand = pygame.image.load("right-hand.png")
s_hand = pygame.image.load("left-hand.png")

m_angle = 0
s_angle = 0

def draw_clock():
    now = datetime.now()
    m_angle = -(now.minute + now.second/60) * 6  
    s_angle = -now.second * 6 

    screen.fill((255, 255, 255))  

    screen.blit(clock_face, (80,50))

    rotated_m_hand = pygame.transform.rotate(m_hand, m_angle)
    m_rect = rotated_m_hand.get_rect(center=(width // 2, height // 2))
    screen.blit(rotated_m_hand, m_rect.topleft)

    rotated_s_hand = pygame.transform.rotate(s_hand, s_angle)
    second_rect = rotated_s_hand.get_rect(center=(width // 2, height // 2))
    screen.blit(rotated_s_hand, second_rect.topleft)

    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    draw_clock()
    pygame.time.delay(1000)  
