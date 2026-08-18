import pygame
from button import Button as B
import random

class Calc:

    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, width, height)
        self.buttons = []
        self.expression = ""
        self.result = 0
        self.target = 0
        self.start = 0
        self.error = False
        self.display_rect = pygame.Rect(self.rect.x + screen_width * 0.025, self.rect.y + screen_height * 0.03125,self.rect.width - screen_width * 0.05,screen_height * 0.09375)
        self.expression_print = self.expression
        self.alvo_font = pygame.font.Font("Assets/fonts/PatrickHand-Regular.ttf", int(screen_width * 1/16))
        self.total_uses = 0
        self.money = 4
        self.screen_flag = True
        self.continue_flag = False
        self.cash_out = 0
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.money_flag = 0

    def gen_round(self, roundnum):

        min_target = 0
        max_target = 0
        flag_int = True

        for button in self.buttons:
            button.price = 2

        if roundnum < 3:
            min_target = 0
            max_target = 30
            self.total_uses = 5
            self.money_gain = 3
        elif roundnum >= 3 and roundnum < 5:
            min_target = 10
            max_target = 50
            self.total_uses = 5
            self.money_gain = 4
        elif roundnum  >= 5 and roundnum < 7:
            min_target = 15
            max_target = 100
            self.total_uses = 6
            self.money_gain = 5
        elif roundnum >= 7 and roundnum < 9:
            min_target = 20.0
            max_target = 100.0
            self.total_uses = 6
            flag_int = False
            self.money_gain = 6
        else:
            min_target = 10.0
            max_target = 500.0
            self.total_uses = 7
            flag_int = False
            self.money_gain = 6

        if flag_int:
            self.target = random.randint(min_target, max_target)

        else:
            self.target = round(random.uniform(min_target, max_target), 2)


        while True:
            self.start = random.randint(0, 30)

            if roundnum >= 5:
                if abs(self.start - self.target) >= 10:
                    break
            else:
                if self.start != self.target:
                    break

        self.expression = str(self.start)
        self.expression_print = self.expression

    def add_button(self, button):
        self.buttons.append(button)

    def draw(self, screen, font, usesfont, end_flag):

        if self.error == True:
            font_surf = font.render("ERRO", False, "Black")
        else:
            font_surf = font.render(self.expression_print, False, "Black")

        font_rect = font_surf.get_rect(midright=(self.display_rect.right - self.screen_width * 1/80, self.display_rect.centery))
        self.alvo_surf = self.alvo_font.render(f"ALVO: {self.target}", False, "Black")
        self.alvo_rect = self.alvo_surf.get_rect(center = (self.screen_width * 0.5, self.screen_height * 0.078125))
        self.usos_surf = self.alvo_font.render(f"USOS RESTANTES: {self.total_uses}", False, "Black")
        self.usos_rect = self.alvo_surf.get_rect(center = (self.screen_width * 0.38125, self.screen_height * 0.15625))


        pygame.draw.rect(screen, (160, 160, 160), self.rect, border_radius=20)

        pygame.draw.rect(screen, (180, 220, 180), self.display_rect, border_radius=8)

        if not end_flag:
            screen.blit(font_surf, font_rect)
            screen.blit(self.alvo_surf, self.alvo_rect)
            screen.blit(self.usos_surf, self.usos_rect)
        

        for button in self.buttons:
            button.draw(screen, font, usesfont)

    def check_click(self, mouse_pos): 
        for button in self.buttons: 
            if button.is_clicked(mouse_pos, True):

                if self.total_uses >= 0:
                    label = button.use()

                    if self.total_uses <= 0:
                        if label != False and label != "=":
                            button.uses += 1
                            return "game over"

                    if label != False and label in "+-*/":
                        if self.expression and self.expression[-1] in "+-*/":
                            button.uses += 1
                            return False

                    if label != False and label == "0":
                        if self.expression and self.expression[-1] in "+-*/":
                            self.expression_print += label
                            return False

                    if label != "=" and label != False: 
                        self.expression += label 

                    if label != "=" and label != "*" and label != "/" and label != False and label != '.': 
                        self.expression_print += label 
                    elif label == "/": 
                        self.expression_print += "÷" 
                    elif label == "*": 
                        self.expression_print += "x" 
                    elif label == '.': 
                        self.expression_print += ',' 

                    if self.error == True: 
                        self.error = False 

                    if label != '=' and label != False: 
                        self.total_uses -= 1 

                    return label

        return False

    def blur_surface(self, screen, scale=8):
        small = pygame.transform.smoothscale(
        screen,
        (screen.get_width() // scale, screen.get_height() // scale)
        )

        return pygame.transform.smoothscale(
        small,
        screen.get_size()
        )


    def get_result(self):

        try:
            self.result = round(float(eval(self.expression)), 2)

            if int(self.result) == self.result:
                self.result = int(self.result)

        except(SyntaxError, ZeroDivisionError):
            self.result = None
            self.error = True


    def get_end(self):

        self.get_result()

        self.cash_out = 0

        if self.result is not None:
            self.expression = str(self.result)
            self.expression_print = self.expression

        if self.result == self.target:
            if self.money > 25:
                self.temp_money = 25
            else:
                self.temp_money = self.money
                self.money += int(self.temp_money / 5)
            self.money += self.money_gain
            self.money += self.total_uses

            self.cash_out += int(self.temp_money / 5)
            self.cash_out += self.money_gain
            self.cash_out += self.total_uses


        return self.result == self.target

    def game_win_sequence(self, time, start_time, screen, money_sound):

        end_time = 8000

        if int(self.temp_money/ 5) <= 0:
            end_time = 6000

        if time - start_time >= 2000:
            end_surf1 = self.alvo_font.render(f"Dinheiro da rodada: R${self.money_gain}", False, "Black")
            end_rect1 = end_surf1.get_rect(center = (self.screen_width * 0.5, self.screen_height * 75/640))
            screen.blit(end_surf1, end_rect1)
            if self.money_flag == 0:
                self.money_flag += 1
                money_sound.play()
        if time - start_time >= 4000:
            end_surf2 = self.alvo_font.render(f"Usos sobrando: R${self.total_uses}", False, "Black")
            end_rect2 = end_surf2.get_rect(center = (self.screen_width * 0.5, self.screen_height * 175/640))
            screen.blit(end_surf2, end_rect2)
            if self.money_flag == 1:
                self.money_flag += 1
                money_sound.play()
        if time - start_time >= 6000:
                end_surf3 = self.alvo_font.render(f"Juros: R${int(self.temp_money / 5)}", False, "Black")
                end_rect3 = end_surf3.get_rect(center = (self.screen_width * 0.5, self.screen_height * 275/640))
                if self.temp_money >= 5:
                    screen.blit(end_surf3, end_rect3)
                    if self.money_flag == 2:
                        self.money_flag += 1
                        money_sound.play()
        if time - start_time >= end_time:
            game_continue_surf = self.alvo_font.render(f"Pagamento: R${self.cash_out}", False, "White")

            if self.temp_money >= 5:
                if self.money_flag == 3:
                    self.money_flag += 1
                    money_sound.play()
            else:
                if self.money_flag == 2:
                    self.money_flag += 1
                    money_sound.play()

            game_continue_rect = game_continue_surf.get_rect(center = (self.screen_width * 0.5, self.screen_height * 375/640))

            if not game_continue_rect.collidepoint(pygame.mouse.get_pos()):
                        self.continue_flag = False
            
            screen.blit(game_continue_surf, game_continue_rect)
            
            pygame.draw.rect(screen, "Black", game_continue_rect, width=0, border_radius=8)
            
            screen.blit(game_continue_surf, game_continue_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        return "Quit"
            if time - start_time >= end_time:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if game_continue_rect.collidepoint(pygame.mouse.get_pos()):
                            self.continue_flag = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if game_continue_rect.collidepoint(pygame.mouse.get_pos()) and self.continue_flag:
                        self.money_flag = 0
                        return False
        return True
        

    def draw(self, screen, font, usesfont, end_flag):
    
            if self.error == True:
                font_surf = font.render("ERRO", False, "Black")
            else:
                font_surf = font.render(self.expression_print, False, "Black")

    
            font_rect = font_surf.get_rect(midright=(self.display_rect.right - self.screen_width * 1/80, self.display_rect.centery))
            self.alvo_surf = self.alvo_font.render(f"ALVO: {self.target}", False, "Black")
            self.alvo_rect = self.alvo_surf.get_rect(center = (self.screen_width * 0.5, self.screen_height * 5/64))
            self.usos_surf = self.alvo_font.render(f"USOS RESTANTES: {self.total_uses}", False, "Black")
            self.usos_rect = self.alvo_surf.get_rect(center = (self.screen_width * 305/800, self.screen_height * 10/64))

            self.font = font
    
    
            pygame.draw.rect(screen, (160, 160, 160), self.rect, border_radius=20)
    
            pygame.draw.rect(screen, (180, 220, 180), self.display_rect, border_radius=8)
    
            if not end_flag:
                screen.blit(font_surf, font_rect)
                screen.blit(self.alvo_surf, self.alvo_rect)
                screen.blit(self.usos_surf, self.usos_rect)

            self.uses_font = usesfont
    
            for button in self.buttons:
                button.draw(screen, font, usesfont, True)
    
    def check_click_shop(self, mouse_pos):
        for button in self.buttons:
            if button.is_clicked(mouse_pos, False): 

                if self.money >= button.price:
                    self.money -= button.buy_button()
    
                return True
    
        return False

    def create_start_buttons(self):

        layout = [("0", 0, 3), ("1", 0, 0), ("2", 1, 0), ("3", 2, 0),
                  ("4", 0, 1), ("5", 1 , 1), ("6", 2, 1), ("7", 0, 2),
                  ("8", 1, 2), ("9", 2, 2), ("+", 3, 0), ("-", 3, 1),
                  ("/", 3, 3), ("*",  3, 2), ("=", 2, 3), (".", 1, 3)]

        button_width = self.screen_width * 6/80
        button_height = button_width
        button_uses = 2

        start_x = self.rect.x + self.screen_width * 0.9/40
        start_y = self.rect.y + self.screen_height * 1.12/8

        start_shop_x = self.screen_width * 7/80
        start_shop_y = self.screen_height * 17/64

        sep = self.screen_width * 1/80

        for label, col, row in layout:

            if label.isdigit():
                price = 3
            else:
                price = 2

            x = start_x + col * (button_width + sep)
            y = start_y + row * (button_height + sep)

            shop_x = start_shop_x + col * (button_width + self.screen_width * 7/40)
            shop_y = start_shop_y + row * (button_width + self.screen_height * 1/16)

            if label == "/":
                shop_x -= (button_width + self.screen_width * 7/40)

            button = B(label, x, y, button_width, button_height, price, button_uses, shop_x, shop_y)

            self.buttons.append(button)

    def draw_shop(self, screen):

        self.money_surf = self.alvo_font.render(f"Seu dinheiro: R${self.money}", False, "Black")
        self.money_rect = self.money_surf.get_rect(center = (self.screen_width * 0.5, self.screen_height * 5/64))

        screen.blit(self.money_surf, self.money_rect)

        for button in self.buttons:
            if button.label != "=":

                if not button.is_clicked(pygame.mouse.get_pos(), False):
                    button.is_pressed = False
                
                button.draw(screen, self.font, self.uses_font, False)

                price_surf = self.uses_font.render(f"R${button.price}", False, "Black")

                price_rect = price_surf.get_rect(midtop=(button.shop_rect.centerx, button.shop_rect.bottom + 5))
                
            screen.blit(price_surf, price_rect)