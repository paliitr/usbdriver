import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class TextPrint:
    def __init__(self):
        self.reset()
        self.font = pygame.font.Font(None, 20)

    def printer(self, screen, textString):
        textBitmap = self.font.render(textString, True, BLACK)
        screen.blit(textBitmap, [self.x, self.y])
        self.y += self.line_height
        
    def reset(self):
        self.x = 10
        self.y = 10
        self.line_height = 15
        
    def indent(self):
        self.x += 10
       
    def unindent(self):
        self.x -= 10
   
pygame.init()
size = [500, 700]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Team Robocon IITR")
done = False
clock = pygame.time.Clock()
pygame.joystick.init()
textPrint = TextPrint()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
    screen.fill(WHITE)
    textPrint.reset()
    joystick_count = pygame.joystick.get_count()

    textPrint.printer(screen, "Number of joysticks: {}".format(joystick_count))
    textPrint.indent()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
    
        textPrint.printer(screen, "Joystick {}".format(i))
        textPrint.indent()
    
        name = joystick.get_name()
        textPrint.printer(screen, "Joystick name: {}".format(name))
        
        axes = joystick.get_numaxes()
        textPrint.printer(screen, "Number of axes: {}".format(axes))
        textPrint.indent()
        
        for i in range(axes):
            axis = joystick.get_axis(i)
            textPrint.printer(screen, "Axis {} value: {:>6.3f}".format(i, axis))
        textPrint.unindent()
            
        buttons = joystick.get_numbuttons()
        textPrint.printer(screen, "Number of buttons: {}".format(buttons))
        textPrint.indent()

        for i in range(buttons):
            button = joystick.get_button(i)
            textPrint.printer(screen, "Button {:>2} value: {}".format(i, button))
        textPrint.unindent()
            
        hats = joystick.get_numhats()
        textPrint.printer(screen, "Number of hats: {}".format(hats))
        textPrint.indent()

        for i in range(hats):
            hat = joystick.get_hat(i)
            textPrint.printer(screen, "Hat {} value: {}".format(i, str(hat)))
        textPrint.unindent()
        
        textPrint.unindent()

    pygame.display.flip()
    clock.tick(200)
pygame.quit()

