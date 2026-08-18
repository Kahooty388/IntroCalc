import pygame

class Button:
    def __init__(self, label, x, y, width, height, price, uses, shop_x, shop_y):
        self.label = label
        self.x = x
        self.y = y
        self.shop_x = shop_x
        self.shop_y = shop_y
        self.rect = pygame.Rect(x, y, width, height)
        self.shop_rect = pygame.Rect(shop_x, shop_y, width, height)
        self.width = width
        self.height = height
        self.is_pressed = False

        self.price = price
        self.uses = uses
        self.color = "black"

    def draw(self, screen, font, uses_font, game_flag):

        uses_surf = uses_font.render(str(self.uses), False, "Red")
        if game_flag:
            uses_rect = uses_surf.get_rect(center = self.rect.topright)
        else:
            uses_rect = uses_surf.get_rect(center = self.shop_rect.topright)

        if self.label != "*" and self.label != "/" and self.label != ".":

            font_surf = font.render(self.label, False, "Black")

        elif self.label == "*":
            font_surf = font.render("X", False, "Black")

        elif self.label == "/":
            font_surf = font.render("÷", False, "Black")

        elif self.label == ".":
            font_surf = font.render(",", False, "Black")

        if game_flag:
            font_rect = font_surf.get_rect(center = self.rect.center)
        else:
            font_rect = font_surf.get_rect(center = self.shop_rect.center)

        if self.is_pressed:
            if game_flag:
                pygame.draw.rect(screen, (180, 180, 180), self.rect, border_radius=8)
            else:
                pygame.draw.rect(screen, (180, 180, 180), self.shop_rect, border_radius=8)

        else:
            if game_flag:
                pygame.draw.rect(screen, (230, 230, 230), self.rect, width=0, border_radius=8)
            else:
                pygame.draw.rect(screen, (230, 230, 230), self.shop_rect, border_radius=8)

        if game_flag:
            pygame.draw.rect(screen, "black", self.rect, width=2, border_radius=8)
        else:
            pygame.draw.rect(screen, "black", self.shop_rect, width=2, border_radius=8)

        screen.blit(font_surf, font_rect)

        if self.label != "=":
            screen.blit(uses_surf, uses_rect)

    def is_clicked(self, pos, game_flag):
        if game_flag:
            self.is_pressed = self.rect.collidepoint(pos)
        else:
            self.is_pressed = self.shop_rect.collidepoint(pos)

        return self.is_pressed

    def use(self):
        if self.uses > 0:

            if self.label != "=":
                self.uses -= 1

            return self.label

        else:
            return False
        
    def buy_button(self):
        self.uses += 1
        self.price += 1
        
        return self.price - 1