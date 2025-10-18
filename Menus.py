import pygame

class StartMenu:
    def __init__(self, screen, HEIGHT=600, WIDTH=800):
        self.screen = screen
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.font = pygame.font.Font(None, 74)
        self.load_text = self.font.render("Load Game", True, (255, 255, 255))
        self.start_text = self.font.render("Start Game", True, (255, 255, 255))
        self.quit_text = self.font.render("Quit", True, (255, 255, 255))
        # Berechne die Rechtecke für die Buttons
        self.start_rect = self.start_text.get_rect(center=(self.WIDTH // 2, 250))
        self.quit_rect = self.quit_text.get_rect(center=(self.WIDTH // 2, 350))
        self.load_rect = self.load_text.get_rect(center=(self.WIDTH // 2, 150))

    def draw(self):
        self.screen.fill((0, 0, 0))  # Fill the screen with black

        # Titeltext
        self.screen.blit(self.load_text, self.load_rect)
        # Verwende die gespeicherten start_rect und quit_rect
        self.screen.blit(self.start_text, self.start_rect)
        self.screen.blit(self.quit_text, self.quit_rect)
        pygame.display.flip()  # Update the display

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # Prüfe, ob die Maus im Bereich des Textes ist
            if self.load_rect.collidepoint(mouse_pos):
                print("Load Game clicked")
                # Hier könnte Logik zum Laden eines Spiels hinzugefügt werden
            elif self.start_rect.collidepoint(mouse_pos):
                print("Start Game clicked")
                return "startgame"  # Menü verlassen und StartgameMenu anzeigen
            elif self.quit_rect.collidepoint(mouse_pos):
                print("Quit clicked")
                pygame.quit()
                exit()
        return False


class StartgameMenu:
    def __init__(self, screen, HEIGHT=600, WIDTH=800):
        self.screen = screen
        self.HEIGHT = HEIGHT
        self.WIDTH = WIDTH
        self.font = pygame.font.Font(None, 48)
        self.small_font = pygame.font.Font(None, 36)
        # Name-Eingabe
        self.input_active = False
        self.input_text = ""
        self.input_box = pygame.Rect(self.WIDTH // 2 - 150, 120, 300, 50)
        # Schwierigkeit
        self.difficulties = ["Leicht", "Mittel", "Schwer"]
        self.selected_difficulty = 0
        self.diff_boxes = [pygame.Rect(self.WIDTH // 2 - 150 + i*110, 220, 100, 50) for i in range(3)]
        # Debug Checkbox
        self.debug = False
        self.debug_box = pygame.Rect(self.WIDTH // 2 - 150, 300, 30, 30)
        # Buttons
        self.create_box = pygame.Rect(self.WIDTH // 2 - 150, 380, 140, 50)
        self.back_box = pygame.Rect(self.WIDTH // 2 + 10, 380, 140, 50)

    def draw(self):
        self.screen.fill((30, 30, 30))
        # Name Label
        name_label = self.small_font.render("Weltname:", True, (255,255,255))
        self.screen.blit(name_label, (self.input_box.x, self.input_box.y - 35))
        # Name Eingabefeld
        pygame.draw.rect(self.screen, (255,255,255), self.input_box, 2)
        input_surf = self.font.render(self.input_text or "Name eingeben...", True, (200,200,200) if not self.input_text else (255,255,255))
        self.screen.blit(input_surf, (self.input_box.x+10, self.input_box.y+8))
        # Schwierigkeit
        diff_label = self.small_font.render("Schwierigkeit:", True, (255,255,255))
        self.screen.blit(diff_label, (self.input_box.x, 200))
        for i, box in enumerate(self.diff_boxes):
            color = (100,200,100) if i == self.selected_difficulty else (80,80,80)
            pygame.draw.rect(self.screen, color, box, border_radius=8)
            pygame.draw.rect(self.screen, (255,255,255), box, 2, border_radius=8)
            diff_text = self.small_font.render(self.difficulties[i], True, (255,255,255))
            text_rect = diff_text.get_rect(center=box.center)
            self.screen.blit(diff_text, text_rect)
        # Debug Checkbox
        debug_label = self.small_font.render("Debug-Modus", True, (255,255,255))
        self.screen.blit(debug_label, (self.debug_box.x + 40, self.debug_box.y))
        pygame.draw.rect(self.screen, (255,255,255), self.debug_box, 2)
        if self.debug:
            pygame.draw.rect(self.screen, (0,255,0), self.debug_box.inflate(-6,-6))
        # Buttons
        for box, text in [(self.create_box, "Erstellen"), (self.back_box, "Zurück")]:
            pygame.draw.rect(self.screen, (60,60,60), box, border_radius=8)
            pygame.draw.rect(self.screen, (255,255,255), box, 2, border_radius=8)
            btn_text = self.small_font.render(text, True, (255,255,255))
            text_rect = btn_text.get_rect(center=box.center)
            self.screen.blit(btn_text, text_rect)
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_box.collidepoint(event.pos):
                self.input_active = True
            else:
                self.input_active = False
            for i, box in enumerate(self.diff_boxes):
                if box.collidepoint(event.pos):
                    self.selected_difficulty = i
            if self.debug_box.collidepoint(event.pos):
                self.debug = not self.debug
            if self.create_box.collidepoint(event.pos):
                print(f"Welt erstellen: Name={self.input_text}, Schwierigkeit={self.difficulties[self.selected_difficulty]}, Debug={self.debug}")
                return {"action": "create", "name": self.input_text, "difficulty": self.difficulties[self.selected_difficulty], "debug": self.debug}
            if self.back_box.collidepoint(event.pos):
                return {"action": "back"}
        if event.type == pygame.KEYDOWN and self.input_active:
            if event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            elif event.key == pygame.K_RETURN:
                self.input_active = False
            elif len(self.input_text) < 20 and event.unicode.isprintable():
                self.input_text += event.unicode
        return None
