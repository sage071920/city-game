import pygame
from Menus import StartMenu, StartgameMenu  # StartgameMenu importieren

class Game:
    def __init__(self):
        pygame.init()
        self.HEIGHT = 600
        self.WIDTH = 800
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("City Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.start_menu = StartMenu(self.screen, self.HEIGHT, self.WIDTH)
        self.startgame_menu = StartgameMenu(self.screen, self.HEIGHT, self.WIDTH)  # StartgameMenu Instanz
        self.screen.fill((0, 0, 0))  # Fill the screen with black

    def show_start_menu(self):
        menu_active = True
        while menu_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # handle_event gibt True zurück, wenn das Menü verlassen werden soll
                if self.start_menu.handle_event(event):
                    menu_active = False
            self.start_menu.draw()
            self.clock.tick(60)

    def show_startgame_menu(self):
        menu_active = True
        while menu_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                result = self.startgame_menu.handle_event(event)
                if result:
                    if result.get("action") == "back":
                        menu_active = False  # Zurück zum Hauptmenü
                    elif result.get("action") == "create":
                        # Hier könnte das Spiel gestartet werden
                        print("Spielstart mit:", result)
                        menu_active = False
            self.startgame_menu.draw()
            self.clock.tick(60)

    def run(self):
        while True:
            self.show_start_menu()
            self.show_startgame_menu()


if __name__ == "__main__":
    game = Game()
    game.run()