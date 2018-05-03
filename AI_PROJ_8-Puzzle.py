import heapq
# import sys
# sys.setrecursionlimit(3500)

def print_matrix(array_list):
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in array_list]))

def find_Address(puzzle, col, row):
    the_num_have_to_be = (row * 3) + col
    count = 0
    for i in range(3):
        for j in range(3):
            if the_num_have_to_be == puzzle[i][j]:
                temp = (abs(i - row) + abs(j - col))
                count += temp
                # print(count)
                return count


def find_Empty_Row_Col(Matrix):
    # print_matrix(Matrix)
    for i in range(int(3)):
        for j in range(int(3)):
            # print(Matrix[i][j])
            if Matrix[i][j] == 0:
                return j,i

def count_H_N(puzzle):
    sum_1 = 0
    puzz_count = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != puzz_count:
                # print("***********************")
                # print_matrix(puzzle)
                # print("####")
                temp = find_Address(puzzle, j, i)
                # print(temp)
                # print("***************************")
                sum_1 += temp
            
            # print(puzz_count)
            puzz_count+=1
        
    # print("*********************************")
    # print_matrix(puzzle)
    # print(sum_1)
    # print("*****************************")
            
    return sum_1


def count_H_N_2(puzzle):
    col_address, row_address = find_Empty_Row_Col(puzzle)
    diff = col_address + row_address + 2
    return diff
    



def build_distination(x, y):
    Mat_dis = [[0 for i in range(3)] for j in range(3)] 
    # print(Mat_dis)
    sum = 0
    # print("hello")
    for i in range (x):
        for j in range (y):
            Mat_dis[i][j] = sum
            sum += 1    
    return Mat_dis



class Vertex:
    def __init__(self, puzzle, name, g_n=0, h_n=0, parent=None):
        self.v_name = name
        self.v_puzzle = puzzle
        self.goal_Mode = self.goal_Check()
        self.color = 'Black'
        self.parent = parent
        self.neighbours = list()
        self.col, self.row = find_Empty_Row_Col(self.v_puzzle)
        self.g_n = g_n
        self.h_n = h_n
        self.f_n = self.g_n + self.h_n


    def goal_Check(self):
        self.goal_Mode = True
        # goal_Mat = build_distination(3, 3)
        goal_dis = 0
        for i in range(3):
            for j in range(3):
                # if self.v_puzzle[int(i)][int(j)] == goal_dis:
                #     self.goal_Mode = True
                if self.v_puzzle[i][j] != goal_dis:
                    self.goal_Mode = False
                    # return False
                goal_dis+=1
        if self.goal_Mode == True:
            return self.goal_Mode

        else:
            com_mat = [[2,1,0],[5,4,3],[8,7,6]]
            for i in range(3):
                for j in range(3):
                    if self.v_puzzle[i][j] == com_mat[i][j]:
                        self.goal_Mode = True
                    else:
                        self.goal_Mode = False
                        return self.goal_Mode
                    
        return self.goal_Mode


    def copy_Puzzle(self):
        copy_Puzz = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                copy_Puzz[i][j] = self.v_puzzle[i][j]

        return copy_Puzz


    def move_Puzzle_Right(self):
        puzz_R = self.copy_Puzzle()
        if self.col < 2:
            # print("Moving Right...")
            temp_R = puzz_R[self.row][self.col+1]
            puzz_R[self.row][self.col+1] = puzz_R[self.row][self.col]
            puzz_R[self.row][self.col] = temp_R
            return puzz_R
        else:
            # print("Can't Move Right! col = {0}".format(self.col))
            return False

    def move_Puzzle_Up(self):
        puzz_U = self.copy_Puzzle()
        if self.row > 0:
            # print("Moving Up...")
            temp_U = puzz_U[self.row-1][self.col]
            puzz_U[self.row-1][self.col] = puzz_U[self.row][self.col]
            puzz_U[self.row][self.col] = temp_U
            return puzz_U
        else:
            # print("can't Move Up! row = {0}".format(self.row))
            return False


    def move_Puzzle_Down(self):
        puzz_D = self.copy_Puzzle()
        if self.row < 2:
            # print("Moving Down...")
            temp_D = puzz_D[self.row+1][self.col]
            puzz_D[self.row+1][self.col] = puzz_D[self.row][self.col]
            puzz_D[self.row][self.col] = temp_D
            return puzz_D
        else:
            # print("Can't Move Down! Row = {0}".format(self.row))
            return False


    def move_Puzzle_Left(self):
        puzz_L = self.copy_Puzzle()
        if self.col > 0:
            # print("Moving Left...")
            temp_V = puzz_L[self.row][self.col-1]
            puzz_L[self.row][self.col-1] = puzz_L[self.row][self.col]
            puzz_L[self.row][self.col] = temp_V
            return puzz_L

        else:
            # print("Can't Move Left! Col = {0}".format(self.col))
            return False

    def __str__(self):
        return self.v_name

    # def __lt__(self, other):
    #     # print("hello!!!")
    #     return self.f_n < other.f_n

priority_Queue = []
node_Creation_Counter = 0
class Tree:
    def __init__(self, puzzle, counter = 0):
        global node_Creation_Counter
        self.main = Vertex(puzzle, counter)
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        node_Creation_Counter += 1

    def A_Star(self, a_star=True):
        # global node_Creation_Counter
        counter = 0
        heapq.heappush(priority_Queue, self)
        while self.main.goal_Mode != True:
            counter += 1
            # if self.main.move_Puzzle_Up() != False:
            #     self.up = Tree(self.main.move_Puzzle_Up())
            #     # Vertex(self.main.move_Puzzle_Up(), counter)
            #     h_n_up = count_H_N(self.up.main.v_puzzle)
            #     self.up.main.h_n = h_n_up
            #     if (a_star == True):
            #         self.up.main.g_n += (1+self.main.g_n)

            #     self.up.main.f_n = self.up.main.h_n + self.up.main.g_n
            #     # self.up.main.parent = self.main
            #     heapq.heappush(priority_Queue, self.up)

            #     counter+=1
                
            # if self.main.move_Puzzle_Down() != False:
            #     self.down = Tree(self.main.move_Puzzle_Down())
            #     # Vertex(self.main.move_Puzzle_Down(), counter)
            #     h_n_down = count_H_N(self.down.main.v_puzzle)
            #     self.down.main.h_n = h_n_down
            #     if (a_star == True):
            #         self.down.main.g_n += (1+self.main.g_n)

            #     self.down.main.f_n = self.down.main.h_n + self.down.main.g_n
            #     # self.down.main.parent = self.main
            #     heapq.heappush(priority_Queue, self.down)
                
            #     counter+=1
            
            # if self.main.move_Puzzle_Left() != False:
            #     self.left = Tree(self.main.move_Puzzle_Left())
            #     # Vertex(self.main.move_Puzzle_Left(), counter)
            #     h_n_left = count_H_N(self.left.main.v_puzzle)
            #     self.left.main.h_n = h_n_left
            #     if (a_star == True):
            #         self.left.main.g_n += (1+self.main.g_n)

            #     self.left.main.f_n = self.left.main.h_n + self.left.main.g_n
            #     # self.left.main.parent = self.main
            #     heapq.heappush(priority_Queue, self.left)
                
            #     counter+=1

            # if self.main.move_Puzzle_Right() != False:
            #     self.right = Tree(self.main.move_Puzzle_Right())
            #     # Vertex(self.main.move_Puzzle_Right(), counter)
            #     h_n_right = count_H_N(self.right.main.v_puzzle)
            #     self.right.main.h_n = h_n_right
            #     if (a_star == True):
            #         self.right.main.g_n += (1+self.main.g_n)

            #     self.right.main.f_n = self.right.main.h_n + self.right.main.g_n
            #     # self.right.main.parent = self.main
            #     heapq.heappush(priority_Queue, self.right)

            #     counter+=1

            check = heapq.heappop(priority_Queue)
            check.main.goal_Mode = check.main.goal_Check()
            if check.main.goal_Mode == True:
                print("Yue Have Finally Reached the Goal !!!")
                print("the Answare id Equal with : ")
                print(check.main.v_name)
                print_matrix(check.main.v_puzzle)
                print("#################################")
                print("The number of the nodes that Created is equal with : {0}.".format(node_Creation_Counter))
                return "Success !!!"
            else:
                # print("helooooo")
                if check.main.move_Puzzle_Up() != False:
                    check.up = Tree(check.main.move_Puzzle_Up())
                    # Vertex(self.main.move_Puzzle_Up(), counter)
                    h_n_up = count_H_N(check.up.main.v_puzzle)
                    check.up.main.h_n = h_n_up
                    if (a_star == True):
                        check.up.main.g_n += (1+check.main.g_n)
                    # print("fdggffd")
                    check.up.main.f_n = check.up.main.h_n + check.up.main.g_n
                    # self.up.main.parent = self.main
                    heapq.heappush(priority_Queue, check.up)
                    # node_Creation_Counter += 1

                    counter+=1
                    
                if check.main.move_Puzzle_Down() != False:
                    check.down = Tree(check.main.move_Puzzle_Down())
                    # Vertex(self.main.move_Puzzle_Down(), counter)
                    h_n_down = count_H_N(check.down.main.v_puzzle)
                    check.down.main.h_n = h_n_down
                    if (a_star == True):
                        check.down.main.g_n += (1+check.main.g_n)

                    check.down.main.f_n = check.down.main.h_n + check.down.main.g_n
                    # self.down.main.parent = self.main
                    heapq.heappush(priority_Queue, check.down)
                    # node_Creation_Counter += 1

                    counter+=1
                
                if check.main.move_Puzzle_Left() != False:
                    check.left = Tree(check.main.move_Puzzle_Left())
                    # Vertex(self.main.move_Puzzle_Left(), counter)
                    h_n_left = count_H_N(check.left.main.v_puzzle)
                    check.left.main.h_n = h_n_left
                    if (a_star == True):
                        check.left.main.g_n += (1+check.main.g_n)

                    check.left.main.f_n = check.left.main.h_n + check.left.main.g_n
                    # self.left.main.parent = self.main
                    heapq.heappush(priority_Queue, check.left)
                    # node_Creation_Counter += 1

                    counter+=1

                if check.main.move_Puzzle_Right() != False:
                    check.right = Tree(check.main.move_Puzzle_Right())
                    # Vertex(self.main.move_Puzzle_Right(), counter)
                    h_n_right = count_H_N(check.right.main.v_puzzle)
                    check.right.main.h_n = h_n_right
                    if (a_star == True):
                        check.right.main.g_n += (1+check.main.g_n)

                    check.right.main.f_n = check.right.main.h_n + check.right.main.g_n
                    # self.right.main.parent = self.main
                    heapq.heappush(priority_Queue, check.right)
                    # node_Creation_Counter += 1

                    counter+=1
            
                # dsff = [[0 for i in range(3)] for j in range(3)]
                # T = Tree(dsff)
                # self = T.main = check

    def __lt__(self, other):
        # print("hello!!!")
        return self.main.f_n < other.main.f_n
                




# def A_Star(self, a_star=True):
#     priority_Queue = []

#     counter = 0
#     while self.main.goal_Mode != True:
#         counter += 1

#         if self.main.move_Puzzle_Up() != False:
#             self.up = Vertex(self.main.move_Puzzle_Up(), counter)
#             h_n_up = count_H_N(self.up.v_puzzle)
#             self.up.h_n = h_n_up
#             if (a_star == True):
#                 self.up.g_n += (1+self.main.g_n)

#             self.up.f_n = self.up.h_n + self.up.g_n
#             self.up.parent = self.main
#             heapq.heappush(priority_Queue, self.up)

#             counter+=1
                
#         if self.main.move_Puzzle_Down() != False:
#             self.down = Vertex(self.main.move_Puzzle_Down(), counter)
#             h_n_down = count_H_N(self.down.v_puzzle)
#             self.down.h_n = h_n_down
#             if (a_star == True):
#                 self.down.g_n += (1+self.main.g_n)

#             self.down.f_n = self.down.h_n + self.down.g_n
#             self.down.parent = self.main
#             heapq.heappush(priority_Queue, self.down)
                
#             counter+=1
            
#         if self.main.move_Puzzle_Left() != False:
#             self.left = Vertex(self.main.move_Puzzle_Left(), counter)
#             h_n_left = count_H_N(self.left.v_puzzle)
#             self.left.h_n = h_n_left
#             if (a_star == True):
#                 self.left.g_n += (1+self.main.g_n)

#             self.left.f_n = self.left.h_n + self.left.g_n
#             self.left.parent = self.main
#             heapq.heappush(priority_Queue, self.left)
                
#             counter+=1

#         if self.main.move_Puzzle_Right() != False:
#             self.right = Vertex(self.main.move_Puzzle_Right(), counter)
#             h_n_right = count_H_N(self.right.v_puzzle)
#             self.right.h_n = h_n_right
#             if (a_star == True):
#                 self.right.g_n += (1+self.main.g_n)

#             self.right.f_n = self.right.h_n + self.right.g_n
#             self.right.parent = self.main
#             heapq.heappush(priority_Queue, self.right)

#             counter+=1

#         check = heapq.heappop(priority_Queue)
#         check.goal_Mode = check.goal_Check()
#         if check.goal_Mode == True:
#             print("Yue Have Finally Reached the Goal !!!")
#             print("the Answare id Equal with : ")
#             print(check.v_name)
#             print_matrix(check.v_puzzle)
#             return "Success !!!"
#         else:
#             T = Tree()
#             self = T.main = check



# T = Tree([[7,2,4],[5,0,6],[8,3,1]])
# s = A_Star(T)

T = Tree([[7,2,4],[5,0,6],[8,3,1]])
s = T.A_Star()
print(s)

# def main():
#     T = Tree([[3,1,2],[6,4,5],[0,7,8]])
#     while True:
#         choose = 0
#         print("please Choose your decision :")
#         print("if you want the A* algorith select option 1 :")
#         print("else if you wanr the greedy algoriyh select 2 :")
#         if choose == 1:
#             s = T.A_Star(True)
        
#         if choose == 2:
#             s = T.A_Star(False)
        
            