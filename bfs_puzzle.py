# Matrix = [[0 for x in range(w)] for y in range(h)]
# import asyncio.PriorityQueue
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

import heapq

# q = Q.PriorityQueue()

def check_items(ar):
    check_flag = []
    for i in range(0,16):
        check_flag.append(False)
    print(check_flag)
    for item in ar:
        for item_2 in item:
            if item_2 == '*':
                check_flag[0] = True
            else:
                index = int(item_2)
                check_flag[index] = True
    
    if False in check_flag:
        return False
    else :
        return True


def find_Empty_Row_Col(Matrix):
    for i in range(int(3)):
        for j in range(int(3)):
            if Matrix[i][j] == 0:
                return j,i

def build_distination(x, y):
    Mat_dis = [[0 for i in range(x)] for j in range(y)] 
    # print(Mat_dis)
    sum = 0
    # print("hello")
    for i in range (x):
        for j in range (y):
            Mat_dis[i][j] = sum
            sum += 1    
    return Mat_dis

def sort_obj_list_g_n(obj_list):
    pass

def print_matrix(array_list):
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in array_list]))

class Vertex:
    def __init__(self, puzzle, name, g_n=0, h_n=0, parent=None):
        self.v_name = name
        self.v_puzzle = puzzle
        self.goal_Mode = self.goal_Check()
        self.neighbors = list()
        self.color = 'black'
        self.parent = parent
        self.col,self.row = find_Empty_Row_Col(self.v_puzzle)
        self.g_n = 0
        self.h_n = 0


    def add_Vertex(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)

    def goal_Check(self):
        # print_matrix(self.v_puzzle)
        goal_Mat = build_distination(3, 3)
        for i in range(3):
            for j in range(3):
                # print(self.v_puzzle[i][j])
                # print(goal_Mat[i][j])
                if self.v_puzzle[i][j] == goal_Mat[i][j]:
                    self.goal_Mode = True
                else:
                    self.goal_Mode = False
                    return False
        return self.goal_Mode

    def copy_Puzzle(self):
        try:
            copy_Puzz = [[0 for i in range(3)] for j in range(3)]
            for i in range(3):
                for j in range(3):
                    copy_Puzz[i][j] = self.v_puzzle[i][j]
                
            # print_matrix(copy_Puzz)
            
            return copy_Puzz
        except:
            print("smth went wrong during the Matrix copying process!!!")

    def move_Puzz_Right(self):
        # pass
        puzz_R = self.copy_Puzzle()
        if self.col < 2:
            print("Moving Right...")
            temp_R = puzz_R[self.row][self.col+1]
            puzz_R[self.row][self.col+1] = puzz_R[self.row][self.col]
            puzz_R[self.row][self.col] = temp_R
            return puzz_R

        else:
            print("can't move Right! col = {0}".format(self.col))
            return False


        
    
    def move_Puzz_Up(self):
        # pass
        puzz_U = self.copy_Puzzle()
        if self.row > 0:
            print("Moving Up...")
            temp_U = puzz_U[self.row-1][self.col]
            puzz_U[self.row-1][self.col] = puzz_U[self.row][self.col]
            puzz_U[self.row][self.col] = temp_U
            return puzz_U

        else:
            print("can't move Up! row = {0}".format(self.row))
            return False

    
    def move_Puzz_Down(self):
        # pass
        puzz_D = self.copy_Puzzle()
        if self.row < 2:
            print("Moving Down...")
            temp_D = puzz_D[self.row+1][self.col]
            puzz_D[self.row+1][self.col] = puzz_D[self.row][self.col]
            puzz_D[self.row][self.col] = temp_D
            return puzz_D
        
        else:
            print("can't move Down! row = {0}".format(self.row))
            return False
    
    def move_Puzz_Left(self):
        # pass
        # puzz_L = [[0 for x in range(3)] for y in range(3)]
        puzz_L = self.copy_Puzzle()
        if self.col > 0:
            print("Moving Left...")
            temo_V = puzz_L[self.row][self.col-1]
            puzz_L[self.row][self.col-1] = puzz_L[self.row][self.col]
            puzz_L[self.row][self.col] = temo_V
            return puzz_L
        
        else:
            print("can't move Left! col = {0}".format(self.col))
            return False

    def __str__(self):
        return self.v_name

    def __lt__(self, other):
        return self.g_n < other.g_n
    # def copy_Puzzle(self):
    #     copy_Puzz = [[0 for i in range(3)] for j in range(3)]
    #     for i in range(3):
    #         for j in range(3):
    #             copy_Puzz[i][j] = self.v_puzzle[i][j]
        
    #     return copy_Puzz



class Tree:
    def __init__(self, puzzle, counter=0):
        self.main = Vertex(puzzle, counter)
        self.left = None
        self.right = None
        self.up = None
        self.down = None



        
    def BFS(self):
        expand = list()
        counter = 0
        expand.append(self.main)
        while self.main.goal_Mode != True:
            counter += 1
            # pass
            if self.main.move_Puzz_Up() != False:
                self.up = Vertex(self.main.move_Puzz_Up(), counter)
                self.up.parent = self.main
                self.main.neighbors.append(self.up)

                # if self.up.goal_Mode == True:
                #     return "Success!!!"

                expand.append(self.up)
                counter+=1
            if self.main.move_Puzz_Down() != False:
                self.down = Vertex(self.main.move_Puzz_Down(), counter)
                self.down.parent = self.main
                self.main.neighbors.append(self.down)

                # if self.down.goal_Mode == True:
                #     return "Success!!!"

                expand.append(self.up)
                counter+=1

            if self.main.move_Puzz_Left() != False:
                self.left = Vertex(self.main.move_Puzz_Left(), counter)
                self.left.parent = self.main
                self.main.neighbors.append(self.left)
                # if self.left.goal_Mode == True:
                #     return "Success!!!"

                expand.append(self.left)
                counter+=1

            if self.main.move_Puzz_Right() != False:
                self.right = Vertex(self.main.move_Puzz_Right(), counter)
                self.right.parent = self.main
                self.main.neighbors.append(self.right)

                expand.append(self.right)
                counter+=1

            check = expand.pop(0)
            check.goal_Mode = check.goal_Check()
            if check.goal_Mode == True:
                print("we Finally find the Target!!! And...")
                print("the Answare is Equal with : ")
                print(check.v_name)
                print_matrix(check.v_puzzle)
                return "Success!!!"
            else:
                self.main = check

    def UCS(self):
        priority_Q = Q.PriorityQueue()
        heap_q = []
        
        counter = 0
        while self.main.goal_Mode != True:
            counter +=1

            if self.main.move_Puzz_Up() != False:
                self.up = Vertex(self.main.move_Puzz_Up(), counter)
                self.up.g_n += (1 + self.main.g_n)
                self.up.parent = self.main
                self.main.neighbors.append(self.up)

                heapq.heappush(heap_q, (self.up))
                counter +=1
            
            if self.main.move_Puzz_Down() != False:
                self.down = Vertex(self.main.move_Puzz_Down(), counter)
                self.down.g_n += (1 + self.main.g_n)
                self.up.parent = self.main
                self.main.neighbors.append(self.down)
                heapq.heappush(heap_q, (self.down))
                counter +=1

            if self.main.move_Puzz_Left() != False:
                self.left = Vertex(self.main.move_Puzz_Right(), counter)
                self.left.g_n += (1 + self.main.g_n)
                self.up.parent = self.main
                self.main.neighbors.append(self.left)

                heapq.heappush(heap_q, (self.right))
                counter +=1

            if self.main.move_Puzz_Right() != False:
                self.right= Vertex(self.main.move_Puzz_Right(), counter)
                self.right.g_n += (1 + self.main.g_n)
                self.up.parent = self.main
                self.main.neighbors.append(self.right)

                heapq.heappush(heap_q, (self.right))
                counter +=1

            check = heapq.heappop(heap_q)
            check.goal_Mode = check.goal_Check()
            if check.goal_Mode == True:
                print("We have finally reched the Goal!!!")
                print("the answare is equal with : ")
                print(check.v_name)
                print_matrix(check.v_puzzle)
                return "Success!!!"
            else:
                self.main = check


            

def file_opening():
    file_name = input("Enter name of your file : ")
    print(file_name)
    file = ''
    try:
        file = open(file_name,"r")
    except :
        print("error in opening file")
        exit()
    # print("hey")
    print(file)
    lines = file.readlines()
    ar = []
    print(ar)
    if(len(lines) != 4):
        print("this program is designed to solve 4*4 8 puzzle")
        exit()

    else:
        for line in lines:
            line = line.replace("\n","")
            item = line.split(" ")           
            ar.append(item)
        status = check_items(ar)
        if(status == False):
            print("error in input file values")
        else:
            board = Board(ar)
            if (board.solvable() == False):
                print("the instance is not solvable")
                exit()

file_opening()

# q2 = []
# heapq.heappush(q2, (30, '3242342334'))
# heapq.heappush(q2, (10, '32422d34'))
# heapq.heappush(q2, (8, '3242dfgfg34'))
# heapq.heappush(q2, (33, '324fgfdv234'))
# heapq.heappush(q2, (73, '324dfv234'))
# sas = heapq.heappop(q2)
# print(sas)
# print(sas[0])
# print(sas[1])


# q = Q.PriorityQueue()
# q.put(10)
# q.put(1)
# q.put(5)
# while not q.empty():
# 	print(q.get())

# class Graph:
    
        # self.list = question_list
        # self.distination = build_distination

# test_mat = [[1,3,4],[5,7,8],[2,0,6]]
# x, y = find_Empty_Row_Col(test_mat)
# print(x)
# print(y)
# print("can't move right! col = {0}".format(3))

# T = Vertex([[1,3,4],[5,7,8],[2,0,6]], '1')
# print(v)
# print(v.goal_Mode)
# s = v.goal_Check()
# print(s)
# print(v.v_name)
# print(print_matrix(v.v_puzzle))
# vp = v.move_Puzz_Left()
# print_matrix(vp)
# print("*********************")
# vs = v.move_Puzz_Down()
# # print_matrix(vs)
# print("*********************")

# vw = v.move_Puzz_Up()
# print_matrix(vw)

# print("*********************")

# vm = v.move_Puzz_Right()
# print_matrix(vm)
# print("*********************")
# s = build_distination(3, 3)
# print_matrix(s)
# T = Tree([[3,1,2],[4,0,5],[6,7,8]])

# T = Tree([[3,1,2],[0,4,5],[6,7,8]])
# T= Tree([[1,3,4],[5,7,8],[2,0,6]])
# s = T.BFS()
# print(s)
# print_matrix(T.main.v_puzzle)

# vb = vm.
# print(vp)
# print_matrix(vp)

# x = build_distination(3, 3)
# print_matrix(x)
# l = list()
# l.append(3)
# l.append(4)
# l.append(5)
# print(l.pop(0))
# import queue
# q = queue.Queue()

# q.put('3')
# q.put("4","6")
# print(q.get())
# print(q.get())

# def main():
#     pass