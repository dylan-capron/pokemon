import pygame

from game import Game
from menu import display_menu

pygame.init()

def main():
    print("Bienvenue dans le monde Pokémon!")
    display_menu()

if __name__ == "__main__":
    game: Game = Game()
    game.run()
