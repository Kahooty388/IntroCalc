import pygame
import ctypes

from calc import Calc as C

ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("IntroCalc")

import os
os.environ['SDL_AUDIODRIVER'] = 'wasapi'

pygame.mixer.pre_init(44100, -16, 2, 256)
pygame.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

screen_width, screen_height = pygame.display.get_surface().get_size()

running = True

music_flag = True

clock = pygame.time.Clock()

button_font = pygame.font.Font("Assets/fonts/VT323-Regular.ttf", int(screen_width * 1/16))

uses_font = pygame.font.Font("Assets/fonts/VT323-Regular.ttf", int(screen_width * 1/32))

menu_font = pygame.font.Font("Assets/fonts/PatrickHand-Regular.ttf", int(screen_width * 1/8))

game_over_font = pygame.font.Font("Assets/fonts/PatrickHand-Regular.ttf", int(screen_width * 1/8))

shop_cont_font = pygame.font.Font("Assets/fonts/PatrickHand-Regular.ttf", int(screen_width * 1/20))

start_surf = menu_font.render("INTROCALC", False, "Black")

start_font_rect = start_surf.get_rect(center = (screen_width * 0.5, screen_height * 15/128))

game_begin_surf = menu_font.render("Começar", False, "White")

game_begin_rect = game_begin_surf.get_rect(center = (screen_width * 0.5, screen_height * 25/64))

shop_cont_surf = shop_cont_font.render("Continuar ->", False, "White")

shop_cont_rect = shop_cont_surf.get_rect(bottomright = (screen_width * 39/40, screen_height * 60/64))

game_over_surf = game_over_font.render("GAME OVER", False, "Red")

game_over_rect = game_over_surf.get_rect(center=(screen_width * 0.5, screen_height * 7/32))

game_state = "menu"

start_flag = False

shop_cont_flag = False

start_time_flag = True

screen_flag = True

game_over_flag = True

game_flag = True

retry_surf = shop_cont_font.render("Tente de novo", False, "White")

retry_rect = retry_surf.get_rect(center=(screen_width * 0.5, screen_height * 35/64))

quit_surf = shop_cont_font.render("Fechar jogo", False, "White")

quit_rect = quit_surf.get_rect(center=(screen_width * 0.5, screen_height * 45/64))

pygame.display.set_caption("IntroCalc")

bg_surface = pygame.image.load("Assets/bg.jpg").convert_alpha()
bg_surface = pygame.transform.scale(bg_surface, screen.get_size())

icon = pygame.image.load("Assets/icon.png").convert_alpha()
pygame.display.set_icon(icon)

click_sound = pygame.mixer.Sound("Assets/sounds/click.wav")

game_over_sound = pygame.mixer.Sound("Assets/sounds/game_over.mp3")

money_get_sound = pygame.mixer.Sound("Assets/sounds/money_get.mp3")

money_flag = 0

round_num = 1

round_flag = True

uses_flag = True

calc = C(screen_width * 25/80, screen_height * 15/64, screen_width * 3/8, screen_height * 5.6/8, screen_width, screen_height)

while running:

    screen.fill("black")

    if game_state == "menu":
        screen.blit(bg_surface, (0,0))

        game_flag = True

        if music_flag:
            pygame.mixer.music.load("Assets/sounds/main_theme.mp3")
            pygame.mixer.music.play(loops=-1, fade_ms=2000)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(loops=-1)
            music_flag = False

        if not game_begin_rect.collidepoint(pygame.mouse.get_pos()):
            start_flag = False

        screen.blit(start_surf, start_font_rect)

        pygame.draw.rect(screen, "Black", game_begin_rect, width=0, border_radius=8)

        screen.blit(game_begin_surf, game_begin_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_begin_rect.collidepoint(pygame.mouse.get_pos()):
                    start_flag = True
            if event.type == pygame.MOUSEBUTTONUP:
                if game_begin_rect.collidepoint(pygame.mouse.get_pos()) and start_flag:
                    game_state = "game"
                    calc.create_start_buttons()


    elif game_state == "shop":

        if game_flag:
            game_flag = False

        screen.blit(bg_surface, (0,0))

        calc.draw_shop(screen)

        pygame.draw.rect(screen, "Black", shop_cont_rect, width=0, border_radius=8)

        screen.blit(shop_cont_surf, shop_cont_rect)


        if not shop_cont_rect.collidepoint(pygame.mouse.get_pos()):
            shop_cont_flag = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos_shop = event.pos

                button_pressed = calc.check_click_shop(mouse_pos_shop)
                if shop_cont_rect.collidepoint(mouse_pos_shop):
                    shop_cont_flag = True
            if event.type == pygame.MOUSEBUTTONUP:

                mouse_pos_shop = event.pos

                if shop_cont_rect.collidepoint(mouse_pos_shop) and shop_cont_flag:
                        game_state = "game"
                        round_flag = True
                                                

    elif game_state == "game":
        
        screen.blit(bg_surface,(0,0))

        if music_flag:
            pygame.mixer.music.load("Assets/sounds/main_theme.mp3")
            pygame.mixer.music.play(loops=-1, fade_ms=2000)
            pygame.mixer.music.set_volume(0.5)
            pygame.mixer.music.play(loops=-1)
            music_flag = False
        

        if round_flag == True:
            calc.gen_round(round_num)
            round_flag = False

        calc.draw(screen, button_font, uses_font, False)

        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    button_pressed = calc.check_click(pygame.mouse.get_pos())
                    if button_pressed != False:
                        click_sound.play()
                        if button_pressed == "=":
                            if calc.get_end():
                                round_num += 1
                                
                                start_time = pygame.time.get_ticks()

                                game_state = "win seque"
                            else:
                                if calc.total_uses <= 0:
                                    game_state = "game over"
                    if button_pressed == "game over":
                        game_state = "game over"
                                    
                if event.type == pygame.MOUSEBUTTONUP:
                    for button in calc.buttons:
                        if button.is_pressed == True:
                            button.is_pressed = False
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if calc.get_end():
                            round_num += 1
                                                        
                            start_time = pygame.time.get_ticks()
                        
                            game_state = "win seque"
                        else:
                            if calc.total_uses <= 0:
                                game_state = "game over"
        for button in calc.buttons:
            if button.uses > 0:
                uses_flag = False
                break

        if uses_flag:
            game_state = "game over"

    elif game_state == "win seque":

        if screen_flag:
            screen.blit(bg_surface, (0,0))
            calc.draw(screen, button_font, uses_font, True)
            blurred_screen = calc.blur_surface(screen, scale=8)

        screen.blit(blurred_screen, (0,0))

        time = pygame.time.get_ticks()
        
        game_seq_flag = calc.game_win_sequence(time, start_time, screen, money_get_sound)

        if game_seq_flag == "Quit":
            running = False
        elif not game_seq_flag:
            game_state = "shop"


    elif game_state == "game over":
        screen.fill("black")

        if game_over_flag:
            pygame.mixer.music.stop()
            game_over_start = pygame.time.get_ticks()
            game_over_flag = False
            game_over_surf.set_alpha(0)
            game_over_sound.play()

        time = pygame.time.get_ticks() - game_over_start

        alpha = min(255, int(time / 5500 * 255))

        game_over_surf.set_alpha(alpha)

        screen.blit(game_over_surf, game_over_rect)

        if time >= 6500:
            pygame.draw.rect(screen, "Black", retry_rect, border_radius=8)
            pygame.draw.rect(screen, "Black", quit_rect, border_radius=8)

            screen.blit(retry_surf, retry_rect)
            screen.blit(quit_surf, quit_rect)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if retry_rect.collidepoint(event.pos):
                    game_state = "game"

                    calc = C(screen_width * 25/80, screen_height * 15/64, screen_width * 3/8, screen_height * 5.6/8, screen_width, screen_height)
                    calc.create_start_buttons()

                    round_num = 1
                    round_flag = True
                    game_over_flag = True
                    music_flag = True

                elif quit_rect.collidepoint(event.pos):
                    running = False
                    

    clock.tick(60)

    pygame.display.flip()

pygame.quit()