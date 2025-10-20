import pygame

class Map:
    def __init__(self, screen, HEIGHT=600, WIDTH=800):
        self.screen = screen
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.offset_x = 0  # Offset für horizontale Bewegung
        self.offset_y = 0  # Offset für vertikale Bewegung
        self.GREY = (56, 56, 56)
        self.WHITE = (255, 255, 255)

    def show_map(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        self.screen.fill((0, 185, 0))  # grüner Hintergrund (Wiese)

        # Straße zeichnen (vertikal)
        street_x = 100 + self.offset_x
        street_y = 10 + self.offset_y
        street_width = 40
        street_height = self.HEIGHT
        street = pygame.Rect(street_x, street_y, street_width, street_height)
        pygame.draw.rect(self.screen, self.GREY, street)

        # gestrichelte Mittellinie
        dash_height = 30   # Länge eines Strichs
        gap = 20           # Abstand zwischen den Strichen
        line_x = street_x + street_width // 2 - 2  # Mitte der Straße

        for y in range(street_y, street_y + street_height, dash_height + gap):
            pygame.draw.rect(self.screen, self.WHITE, (line_x, y, 4, dash_height))

        pygame.display.flip()

    def move_map(self):
        keys = pygame.key.get_pressed()
        # WASD und Pfeiltasten abfragen
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.offset_x -= 5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.offset_x += 5
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.offset_y -= 5
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.offset_y += 5
