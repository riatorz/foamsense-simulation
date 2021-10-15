import pygame
from serial import Serial
ser = Serial('COM12',115200)
if not ser.isOpen():
    ser.open()
print('COM12 is open',ser.isOpen())
# Initializing Pygame
pygame.init()
# Initializing surface
window = pygame.display.set_mode((800,600))
def converter(res):
    resmin = 20000
    simmin = 0

    resmax = 55555
    simmax = 200

    csimulation = simmax-simmin
    csimres = resmax-resmin
    vscaled = float(res-resmin)/float(csimres)
    return round(simmax-(vscaled*csimulation),2)
# Initialing Color
color = (255,255,255)
def window_(height,width):
    window.fill((0,0,0))
    rect = pygame.draw.rect(window, color, pygame.Rect(300, 200, width, height))
    window.blit(pygame.transform.rotate(window, 180), (0, 0))
    pygame.display.update()
# Drawing Rectangle
def main():
    run = True
    i=200
    counter = 0
    clock = pygame.time.Clock()
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pico_data = ser.readline()
        pico_data = pico_data.decode("utf-8","ignore")
        print(pico_data[:-3])
        print(converter(float(pico_data[:-3])))
        window_(converter(float(pico_data[:-3])),200)
    pygame.quit()
if __name__ == "__main__":
    main()

