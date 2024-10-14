from tkinter import Tk, BOTH, Canvas
import time

class Window:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.title("Test123")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.canv = Canvas(self.__root, bg="white", height=height, width=width)
        self.canv.pack(fill=BOTH, expand=1)
        self.running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.running = True
        while self.running == True:
            self.redraw()
    
    def close(self):
        self.running = False

    def draw_line(self, Line, fill_color="black"):
        Line.draw(self.canv, fill_color)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, Point1, Point2):
        self.Point1 = Point1
        self.Point2 = Point2
        self.x1 = Point1.x
        self.x2 = Point2.x
        self.y1 = Point1.y
        self.y2 = Point2.y
        

    def draw(self, Canv, fill_color):
        Canv.create_line(self.x1, self.y1, self.x2, self.y2, fill=fill_color, width=2)


class Cell:
    def __init__(self, win):
        self.l_wall = True
        self.r_wall = True
        self.t_wall = True
        self.b_wall = True
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self._win = win
    
    def draw(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        lb = Point(x1, y1)
        rb = Point(x2, y1)
        lt = Point(x1, y2)
        rt = Point(x2, y2)
        if self.l_wall == True:
            left_wall = Line(lb, lt)
            self._win.draw_line(left_wall, "black")
        if self.r_wall == True:
            right_wall = Line(rb, rt)
            self._win.draw_line(right_wall, "black")
        if self.t_wall == True:
            top_wall = Line(lt, rt)
            self._win.draw_line(top_wall, "black")    
        if self.b_wall == True:
            bottom_wall = Line(lb, rb)
            self._win.draw_line(bottom_wall, "black")     

    def draw_move(self, to_cell, undo=False):
        if undo == False:
            line_color = "red"
        else:
            line_color = "grey"
        m1_x = (self.x1 + self.x2) / 2
        m1_y = (self.y1 + self.y2) / 2
        m2_x = (to_cell.x1 + to_cell.x2) / 2
        m2_y = (to_cell.y1 + to_cell.y2) / 2
        m1 = Point(m1_x, m1_y)
        m2 = Point(m2_x, m2_y)
        self._win.draw_line(Line(m1,m2), line_color)

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells = []

    def _create_cells(self):
        for i in range(0,self.num_cols):
            temp_column = []
            for j in range(0, self.num_rows):
                temp_column.append(Cell(self._win))
            self._cells.append(temp_column)
        for i in range(0,self.num_cols):
            for j in range(0, self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        cx1 = self.x1 + i * self.cell_size_x
        cx2 = self.x1 + (i + 1) * self.cell_size_x        
        cy1 = self.y1 + (j + 1) * self.cell_size_y
        cy2 = self.y1 + j * self.cell_size_y    
        self._cells[i][j].draw(cx1, cx2, cy1, cy2)   

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
        

def main():
    win = Window(1000, 1000)

    maze1 = Maze(10,10,15,15,50,50,win)
    maze1._create_cells()
    # Cell_1_1 = Cell(win)
    # Cell_1_1.r_wall = False
    # Cell_1_1.draw(30,80,30,80)
    # Cell_1_2 = Cell(win)
    # Cell_1_2.l_wall = False
    # Cell_1_2.draw(80,130,30,80)
    # Cell_1_2.draw_move(Cell_1_1)
    # a = Point(5, 5)
    # b = Point(50, 80)
    # a_to_b = Line(a, b)

    # c = Point(300, 170)
    # d = Point(80, 200)
    # c_to_d = Line(c, d)

    # win.draw_line(a_to_b, "red")
    # win.draw_line(c_to_d, "green")
    win.wait_for_close()

if __name__ == "__main__":
    main()