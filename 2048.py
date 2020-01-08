#!/bin/python3
"""
implementation of 2048
"""
import random
import sys
import numpy as np
import pygame
import config

class Game():
    """
    main class
    """
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((config.SCREEN_X, config.SCREEN_Y), 0, 32)
        self.data = np.full((4,4), 0)

    def board(self):
        print(self.data)

    def player_turn(self):
        done = 0
        while done == 0:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    print('Exiting...')
                    sys.exit(0)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_UP]:
                self.move(-1, 0)
                done = 1
            if keys[pygame.K_RIGHT]:
                self.move(0, 1)
                done = 1
            if keys[pygame.K_LEFT]:
                self.move(0, -1)
                done = 1
            if keys[pygame.K_DOWN]:
                self.move(1, 0)
                done = 1

    def check_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.data[i][j] == 0:
                    return 1
        return 0

    def place_numbers(self):
        if self.check_game_over() == 0:
            return 
        done = 0
        while done == 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            if self.data[row][col] == 0:
                num = random.random()
                if num >= 0.9:
                    self.data[row][col] = 4
                else:
                    self.data[row][col] = 2
                done = 1

    def move(self, l, k):
        for i in range(4):
            for j in range(4):
                if self.data[i][j] != 0:
                    if j + k < 4 and j + k >= 0 and k != 0:
                        self.data[i][j + k] = self.data[i][j]
                        self.data[i][j] = 0
                    elif i + l < 4 and i + l >= 0 and l != 0:
                        self.data[i + l][j] = self.data[i][j]
                        self.data[i][j] = 0

    def run(self):
        for i in range(2):
            self.place_numbers()
        self.board()
        while True:
            self.clock.tick(32)
            self.player_turn()
            self.board()
            pygame.display.update()
            #self.place_numbers()
            if self.check_game_over() == 0:
                print("Game over!")
                sys.exit(0)

if __name__ == '__main__':
    Game().run()
