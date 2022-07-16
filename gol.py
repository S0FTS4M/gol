from dataclasses import dataclass
from enum import Enum
from sys import stdout
from time import sleep


class CellState(Enum):
    Dead = 0,
    Alive = 1


@dataclass
class Cell:
    state: CellState
    col: int
    row: int

    def __init__(self, col: int, row: int, state: CellState) -> None:
        self.state = state
        self.col = col
        self.row = row


@dataclass
class Board:
    cells = [[]]
    width: int
    heigth: int

    def check_neighbours_of_cell(self, cell: Cell) -> int:
        res: int = 0
        for row in range(-1, 2):
            for col in range(-1, 2):
                if cell.col + col >= 0 and cell.col + col <= self.width - 1 and cell.row+row >= 0 and cell.row + row <= self.heigth - 1:
                    if col == 0 and row == 0:
                        continue
                    currCell = self.cells[cell.row + row][cell.col + col]
                    if currCell.state == CellState.Alive:
                        res += 1
        return res

    def generate_board(self) -> None:
        for row in range(self.heigth):
            self.cells.append([])
            for col in range(self.width):
                newCell = Cell(
                    col=col, row=row, state=CellState.Dead
                )
                self.cells[row].append(newCell)

    def next_generation(self) -> None:
        newBoard = []
        for row in range(self.heigth):
            newBoard.append([])
            for col in range(self.width):
                curr_cell = self.cells[row][col]
                neighbor_count = self.check_neighbours_of_cell(curr_cell)
                curr_state = CellState.Dead
                if curr_cell.state == CellState.Alive and neighbor_count == 2 or neighbor_count == 3:
                    curr_state = CellState.Alive
                elif curr_cell.state == CellState.Dead and neighbor_count == 3:
                    curr_state = CellState.Alive
                else:
                    curr_state = CellState.Dead

                newCell = Cell(
                    col=col, row=row, state=curr_state
                )
                newBoard[row].append(newCell)
        self.cells = newBoard

    def print_board(self):

        print("\033[3;0H")
        for row in range(self.heigth):
            for col in range(self.width):
                if self.cells[row][col].state == CellState.Dead:
                    print(".", end=" ")
                else:
                    print("#", end=" ")
            print("\n")
        stdout.flush()


@dataclass
class Pattern:
    board: Board

    def toad(self):
        self.board = Board(10, 10)
        self.board.generate_board()

        self.board.cells[5][6].state = CellState.Alive
        self.board.cells[5][5].state = CellState.Alive
        self.board.cells[5][4].state = CellState.Alive

        self.board.cells[6][6-1].state = CellState.Alive
        self.board.cells[6][5-1].state = CellState.Alive
        self.board.cells[6][4-1].state = CellState.Alive

    def blinker(self):
        self.board = Board(10, 10)
        self.board.generate_board()

        self.board.cells[1][3].state = CellState.Alive
        self.board.cells[2][3].state = CellState.Alive
        self.board.cells[2][3].state = CellState.Alive

    def glider(self):
        self.board = Board(10, 10)
        self.board.generate_board()

        self.board.cells[0][2].state = CellState.Alive
        self.board.cells[1][3].state = CellState.Alive
        self.board.cells[2][3].state = CellState.Alive
        self.board.cells[2][2].state = CellState.Alive
        self.board.cells[2][1].state = CellState.Alive

    def inf_pattern(self):
        self.board = Board(10, 10)
        self.board.generate_board()

        self.board.cells[6][1].state = CellState.Alive

        self.board.cells[6][3].state = CellState.Alive
        self.board.cells[5][3].state = CellState.Alive

        self.board.cells[4][5].state = CellState.Alive
        self.board.cells[3][5].state = CellState.Alive
        self.board.cells[2][5].state = CellState.Alive

        self.board.cells[3][7].state = CellState.Alive
        self.board.cells[2][7].state = CellState.Alive
        self.board.cells[1][7].state = CellState.Alive

        self.board.cells[2][8].state = CellState.Alive

    def inf_glider(self):
        self.board = Board(40, 20)
        self.board.generate_board()


board = Board(10, 10)
board.generate_board()
time = 5
while True:
    board.print_board()
    board.next_generation()
    sleep(time)
