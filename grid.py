import pygame
import numpy as np
import random

class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale

        self.columns = int(height/scale)
        self.rows = int(width/scale)

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def random2d_array(self):
        print("Executing Random Patterns!")
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0,1)

    def full_array(self):
        self.grid_array.fill(1)
        self.grid_array.dump('export',allow_pickle=True)

    def fixed2d_array(self):
        self.grid_array[50][50] = 1
        self.grid_array[51][50] = 1
        self.grid_array[52][50] = 1
        self.grid_array[53][50] = 1
        self.grid_array[54][50] = 1

        self.grid_array[50][51] = 1
        self.grid_array[51][51] = 1
        self.grid_array[52][51] = 1
        self.grid_array[53][51] = 1
        self.grid_array[54][51] = 1

        self.grid_array[50][52] = 1
        self.grid_array[51][52] = 1
        self.grid_array[52][52] = 1
        self.grid_array[53][52] = 1
        self.grid_array[54][52] = 1

        self.grid_array[50][53] = 1
        self.grid_array[51][53] = 1
        self.grid_array[52][53] = 1
        self.grid_array[53][53] = 1
        self.grid_array[54][53] = 1

        self.grid_array[50][54] = 1
        self.grid_array[51][54] = 1
        self.grid_array[52][54] = 1
        self.grid_array[53][54] = 1
        self.grid_array[54][54] = 1
    
    def gun(self):
        self.grid_array[10][15] = 1
        self.grid_array[10][16] = 1

        self.grid_array[11][15] = 1
        self.grid_array[11][16] = 1

        self.grid_array[20][15] = 1
        self.grid_array[20][16] = 1
        self.grid_array[20][17] = 1

        self.grid_array[21][14] = 1
        self.grid_array[21][18] = 1

        self.grid_array[22][13] = 1
        self.grid_array[22][19] = 1

        self.grid_array[23][13] = 1
        self.grid_array[23][19] = 1

        self.grid_array[24][16] = 1

        self.grid_array[25][14] = 1
        self.grid_array[25][18] = 1

        self.grid_array[26][15] = 1
        self.grid_array[26][16] = 1
        self.grid_array[26][17] = 1

        self.grid_array[27][16] = 1

        self.grid_array[30][13] = 1
        self.grid_array[30][14] = 1
        self.grid_array[30][15] = 1

        self.grid_array[31][13] = 1
        self.grid_array[31][14] = 1
        self.grid_array[31][15] = 1

        self.grid_array[32][12] = 1
        self.grid_array[32][16] = 1

        self.grid_array[34][11] = 1
        self.grid_array[34][12] = 1
        self.grid_array[34][16] = 1
        self.grid_array[34][17] = 1

        self.grid_array[44][13] = 1
        self.grid_array[44][14] = 1

        self.grid_array[45][13] = 1
        self.grid_array[45][14] = 1

    def ask_for_the_file(self):
        pattern_file = input("Enter the name of the file: ")
        if pattern_file:
            #TODO
            pass
        else:
            print("No Pattern File Given..")


    def Conway(self, off_color, on_color, surface):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(surface, on_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])

        next = np.ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours( x, y)
                if state == 0 and neighbours == 3:
                    next[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next[x][y] = 0
                else:
                    next[x][y] = state
        self.grid_array = next

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
