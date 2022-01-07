import pygame
from life import GameOfLife
from pygame.locals import *
from ui import UI


class GUI(UI):
    def __init__(self, life: GameOfLife, cell_size: int = 10, speed: int = 10) -> None:
        self.cell_size = cell_size
        self.speed = speed
        super().__init__(life)
        self.rows, self.cols = life.rows, life.cols
        self.width, self.height = self.rows * cell_size, self.cols * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_lines(self) -> None:
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def draw_grid(self) -> None:
        for i in range(self.rows):
            for j in range(self.cols):
                if self.life.curr_generation[i][j] == 0:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("white"),
                        (
                            i * self.cell_size,
                            j * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        ),
                    )
                else:
                    pygame.draw.rect(
                        self.screen,
                        pygame.Color("green"),
                        (
                            i * self.cell_size,
                            j * self.cell_size,
                            self.cell_size,
                            self.cell_size,
                        ),
                    )

    def pause(self) -> None:
        paused = True
        clock = pygame.time.Clock()
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        paused = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.life.curr_generation = self.get_click(event.pos)
                elif event.type == pygame.QUIT:
                    pygame.quit()
            self.draw_grid()
            self.draw_lines()

            pygame.display.flip()
            clock.tick(self.speed)

    def get_click(self, pos):
        cell_x, cell_y = pos[0] // self.cell_size, pos[1] // self.cell_size

        self.life.curr_generation[cell_x][cell_y] = 1
        return self.life.curr_generation

    def run(self) -> None:
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.pause()

            self.draw_grid()
            self.draw_lines()
            self.life.step()

            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()
