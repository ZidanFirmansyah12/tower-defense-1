import pygame
from config import *
from game import Game

def show_difficulty_menu():
    selecting = True

    while selecting:
        clock.tick(60)

        screen.fill(BLACK)

        title = font.render("SELECT DIFFICULTY", True, YELLOW)
        screen.blit(title, (WIDTH // 2 - 200, 100))

        easy_text = font.render("1 - EASY (Weak enemies, more money)", True, GREEN)
        normal_text = font.render("2 - NORMAL (Balanced)", True, CYAN)
        hard_text = font.render("3 - HARD (Strong enemies, less money)", True, RED)

        screen.blit(easy_text, (WIDTH // 2 - 280, 250))
        screen.blit(normal_text, (WIDTH // 2 - 280, 350))
        screen.blit(hard_text, (WIDTH // 2 - 280, 450))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return Difficulty.EASY
                elif event.key == pygame.K_2:
                    return Difficulty.NORMAL
                elif event.key == pygame.K_3:
                    return Difficulty.HARD


if __name__ == "__main__":
    difficulty = show_difficulty_menu()

    if difficulty:
        game = Game(difficulty)
        game.run()

    pygame.quit()
