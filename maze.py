
import sys
directions = (0,1),(1,0),(0,-1),(-1,0)
directions_str = "Right","Down","Left","Up"
source_char = 'S'
target_char = 'T'
obstacle = '#'
vacant_char = ' '

#class represent current state
class State(object):
    def __init__(self,i):
        #how we got this state
        self.direction = ""
        #index in the maze of the state
        self.row,self.col = i
        self.index = i
    #appending the current direction to the path
    def set_direcion(self,direct,parent):
        self.direction=parent.get_direction() + direct+" "
    def get_direction(self):
        return self.direction
class Maze(object):
    def __init__(self):
        self.data = []
    def in_limits(self,r,c):
        return (r >=0 and r<self.rows) and (c >=0 and c<self.cols)
    def read_maze(self):
        maze_mat = []
        print("enter your maze: # is obstacle, S = SOURCE, T= TARGET,"
              "PRESS '.' TO STOP")
        for line in sys.stdin:
            if '.' == line.rstrip():
                break
            maze_mat.append(list(line))
        self.data = maze_mat
        self.rows = len(self.data)
        self.cols = len(self.data[0])
    def find_start(self):
        for r,line in enumerate(self.data):
            try:
                return r,line.index(source_char)
            except ValueError:
                pass
    def get(self,r,c):
        return self.data[r][c]
    def get_possible_states(self,state):
        next_steps = []
        for str_d,d in zip(directions_str,directions):
            possible_step_row =state.row + d[0]
            possible_step_col = state.col + d[1]
            if(self.in_limits(possible_step_row,possible_step_col) and self.get(possible_step_row,possible_step_col)!= obstacle):
                new_step = State((possible_step_row,possible_step_col))
                new_step.set_direcion(str_d,state)
                next_steps.append(new_step)
        return next_steps
#find the goal using bfs search
def search(maze):
    visited = [[False for i in range(maze.cols)]for j in range(maze.rows)]
    first_step = maze.find_start()
    first_step_state = State(first_step)
    queue =[]
    queue.append(first_step_state)
    while queue:
        s = queue.pop(0)
        if(maze.data[s.row][s.col] == target_char):
            return s.get_direction()
        next_steps = maze.get_possible_states(s)
        for next_step in next_steps:
            if visited[next_step.row][next_step.col] == False:
                queue.append(next_step)
                visited[next_step.row] [next_step.col] = True
    return ""

if __name__ == '__main__':
    maze = Maze()
    maze.read_maze()
    solution = search(maze)
    if solution:
        print(solution)

