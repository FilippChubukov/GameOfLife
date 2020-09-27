import sys
import pygame
from pygame.locals import *
import argparse

class Life:
    def __init__(self, width: int, height: int, cell: int, game_speed: int, file_name: str):
        self.width = width
        self.height = height
        self.cell_size = cell
        self.screen_size = (width, height)

        self.screen = pygame.display.set_mode(self.screen_size)

        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        self.game_speed = game_speed
        self.start_field = file_name

    # drawing a grid #
    def draw_lines(self) -> None:
        for x in range (0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                (x, 0), (x, self.height))

        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                (0, y), (self.width, y))

    # drawing the field #
    def draw_field(self, field: int) -> None:
        for i in range (self.cell_height):
            for j in range (self.cell_width):
                if field[j][i] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('black'),
                        (j * self.cell_size,i * self.cell_size , self.cell_size, self.cell_size))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'),
                        (j * self.cell_size,i * self.cell_size , self.cell_size, self.cell_size))

    # looking for live neighbours, return count of live neighbours #
    def find_neighbours(self, field: int, h:int, w: int):
        neighbours = [0] * 8
        sum = 0

        if w > 0 and h > 0:
            neighbours[0] = field[w - 1][h - 1]

        if h > 0:
            neighbours[1] = field[w][h - 1]

        if h > 0 and w != (self.cell_width - 1):
            neighbours[2] = field[w + 1][h - 1]

        if w > 0:
            neighbours[3] = field[w - 1][h]

        if w != (self.cell_width - 1):
            neighbours[4] = field[w + 1][h]

        if w > 0 and h != (self.cell_height - 1):
            neighbours[5] = field[w - 1][h + 1]

        if h != (self.cell_height - 1):
            neighbours[6] = field[w][h + 1]

        if w != (self.cell_width - 1) and h != (self.cell_height - 1):
            neighbours[7] = field[w + 1][h + 1]

        for i in neighbours:
            sum += i
        return sum

    # run game #
    def run(self) -> None:
        # current generation of the field, #
        game_field = [[0] * (self.cell_height) for i in range(self.cell_width)]
        # next generation of the field #
        game_field_gen = [[0] * (self.cell_height) for i in range(self.cell_width)]

        # try to open file and read start info #
        try:
            data_file = open(self.start_field)

            for line in data_file:
                res = list(line)
                game_field[int(res[0])][int(res[2])] = 1

        except FileNotFoundError:
            print("Error: file not found.")
            sys.exit(1)
        except ValueError:
            print("Error: wrong data in the file.")
            sys.exit(1)

        # init game field #
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Life')
        self.screen.fill(pygame.Color('white'))
        self.draw_lines()
        self.draw_field(game_field)
        pygame.display.flip() # update screen after changes #

        running = True
        while running:
            # finish if the player is out of the game #
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            # resetting the next-generation list #
            for i in range (self.cell_height):
                for j in range (self.cell_width):
                    game_field_gen[j][i] = 0

            for i in range (self.cell_height):
                for j in range (self.cell_width):
                    # get number of live neighbours of the current cell #
                    res = self.find_neighbours(game_field, i, j)

                    # following the rules of the game we change the values of the next generation cells #
                    if game_field[j][i] == 1:
                        if res == 2 or res == 3:
                             game_field_gen[j][i] = 1
                        else:
                            game_field_gen[j][i] = 0

                    else:
                        if res == 3:

                            game_field_gen[j][i] = 1

                        else:
                            game_field_gen[j][i] = 0

            # draw new field #
            self.draw_field(game_field_gen)
            self.draw_lines()
            pygame.display.flip() # update screen after changes #

            # update current field #
            for i in range (self.cell_height):
                for j in range (self.cell_width):
                    game_field[j][i] = game_field_gen[j][i]


            clock.tick(self.game_speed)

        # end current game #
        pygame.quit()

# args parser #
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--width", nargs = '?', default = '800')
    parser.add_argument("--height", nargs = '?', default = '600')
    parser.add_argument("--cell", nargs = '?', default = '10')
    parser.add_argument("--file")
    parser.add_argument("--game_speed", nargs = '?', default = '10')
    return parser

if __name__ == '__main__':
    # get user arguments #
    parser = createParser()
    args = parser.parse_args()

    # if the user didn't specify the file #
    if args.file == None:
        print("Error: no file in arguments.")
        sys.exit(1)

    # try to use arguments, if it doesn't work, we use the default settings #
    try:
        game = Life(int(args.width), int(args.height), int(args.cell), int(args.game_speed), args.file)
    except ValueError:
        print("Warning : some args are wrong, default settings will be used.")
        game = Life(800, 600, 10, 10, args.file)
    game.run()
