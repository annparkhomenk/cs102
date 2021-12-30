import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copy from previous assignment
        if not randomize:
            return [[0 for i in range(self.rows)] for j in range(self.cols)]
        else:
            return [[random.randint(0, 1) for i in range(self.rows)] for j in range(self.cols)]

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        x, y = cell
        neighs = []
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if 0 <= i < self.cols and 0 <= j < self.rows:
                    neighs.append(self.curr_generation[i][j])
        neighs.remove(self.curr_generation[x][y])
        return neighs

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        new_grid = self.create_grid()
        for i in range(self.cols):
            for j in range(self.rows):
                neighbours = self.get_neighbours((i, j))
                if self.curr_generation[i][j] == 0:
                    if sum(neighbours) == 3:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
                else:
                    if sum(neighbours) < 2 or sum(neighbours) > 3:
                        new_grid[i][j] = 0
                    else:
                        new_grid[i][j] = 1
        return new_grid

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_generations and self.max_generations != float("inf"):
            return self.generations > self.max_generations
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        f = open(f"{filename}").readlines()
        grid = []
        for line in f:
            grid.append(list(map(int, list(line))))
        life = GameOfLife((len(grid), len(grid[0])))
        life.curr_generation = grid
        return life

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        f = open(f"{filename}", "w")
        for line in self.curr_generation:
            f.write("".join(list(map(str, line))))
            f.write("\n")
        f.close()
