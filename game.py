import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Space Game')

sprite = pygame.image.load('rocket.jpg')
sprite_rect = sprite.get_rect()
sprite_rect.center = (250,250)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    window.fill((0,0,0))
    window.blit(sprite, sprite_rect)

    pygame.display.flip()
