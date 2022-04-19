# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pygame

pygame.init()
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('road.png')
car = pygame.image.load('tesla.png')
car = pygame.transform.scale(car, (30, 60))
car_x = 150
car_y = 300
cam_offset_x=0
cam_offset_y=0
drive = True
direction='up'
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drive = False

    cam_x=car_x+cam_offset_x+15
    cam_y=car_y+cam_offset_y+15
    # Drive
    up_px=window.get_at((cam_x,cam_y-25))[0]
    right_px=window.get_at((cam_x+25,cam_y))[0]
    down_px = window.get_at((cam_x, cam_y + 25))[0]
    print(up_px,right_px,down_px)
    # drive trun
    if direction=='up' and up_px!=255 and right_px==255:
        direction='right'
        cam_offset_x=30

        car=pygame.transform.rotate(car,-90)

    if direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        cam_offset_y=30
        cam_offset_x=0
        car_x=car_x+30
        car=pygame.transform.rotate(car,-90)
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_offset_x= 30
        cam_offset_y = 0
        car = pygame.transform.rotate(car, 90)

    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_offset_x = 0
        car = pygame.transform.rotate(car, 90)
    #driving

    if direction== 'up' and up_px==255:
        car_y = car_y - 2
    elif direction=='right' and right_px==255:
        car_x=car_x+2
    elif direction=='down' and down_px==255:
        car_y=car_y+2

    clock.tick(60)
    window.blit(track, (0, 0))
    window.blit(car, (car_x, car_y))

    pygame.draw.circle(window,(0,255,0),(cam_x,cam_y),5,5)
    pygame.display.update()
