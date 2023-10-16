import Maze 

def view(grid):
    if grid[i][j] == Maze.EMPTY:
                print("  ", end = "")
                    
            elif grid[i][j] == Maze.EMPTY:
                print("##", end = "")
                    
            elif grid[i][j] == Maze.EMPTY:
                print("^^", end = "")
                    
            elif grid[i][j] == Maze.EMPTY:
                print("$$", end = "")
                    
            elif grid[i][j] == Maze.EMPTY:
                print("..", end = "")
                    
            else:
                raise AssertionError
