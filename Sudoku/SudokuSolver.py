class SudokuSolver:

    def __init__(self, board):
        self.board = board

    def output_board(self):
        for row in self.board:
            print(row)

    def set_val(self, pos: tuple, val: int):
        self.board[pos[0]][pos[1]] = val
    
    def get_val(self, pos: tuple) -> int:
        return self.board[pos[0]][pos[1]]
    
    def get_board(self):
        return self.board

    def find_any_empty(self):
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.get_val((row, col)) == 0:
                    return (row, col) # Position of empty space on board
        return None
    
    def check_row(self, num: int, pos: tuple) -> bool:
        for i in range(len(self.board[0])):

            # Check row for exisiting 'num' value
            if self.get_val((pos[0], i)) == num and pos[1] != i:
                return False
        return True
    
    def check_col(self, num: int, pos: tuple) -> bool:
        for i in range(len(self.board)):

            # Check column for existing 'num' value
            if self.get_val((i, pos[1])) == num and pos[0] != i:
                return False
        return True
    
    def check_box(self, num: int, pos: tuple) -> bool:
        # Initially establish which box the position is in
        box_x = pos[1] // 3
        box_y = pos[0] // 3
        box = (box_x * 3, box_y * 3)

        # Allow for full height and width of box (3x3)
        for row in range(box[1], box[1] + 3): 
            for col in range(box[0], box[0] + 3):
                
                # Check full box for existing 'num' value
                if self.get_val((row, col)) == num and (row, col) != pos:
                    return False
        return True
    
    def check_validity(self, num: int, pos: tuple) -> bool:
        if self.check_row(num, pos) and self.check_col(num, pos) and self.check_box(num, pos):
            return True

    def solve(self):
        #print("Point A")
        empties_left = self.find_any_empty()
        if not empties_left:
            #print("Point END")
            return True
        else:
            #print("Point B")
            row = empties_left[0]
            col = empties_left[1]
        
        for i in range(1,10):
            #print("Point C")

            if self.check_validity(i, (row, col)):
                # (row, col) is a valid position 
                self.set_val((row, col), i)

                if self.solve(): # If there are no more empties
                    return True
                
                self.set_val((row, col), 0)
        return False