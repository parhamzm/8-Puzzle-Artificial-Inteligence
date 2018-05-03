# Matrix = [[0 for x in range(w)] for y in range(h)]
# import asyncio.PriorityQueue
from colored import fg, bg, attr
import cProfile
import colored
from colored import stylize

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

import heapq

# q = Q.PriorityQueue()
def copy_Puzzle(puzzle):
    copy_Puzz = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            # print("helooo")
            copy_Puzz[i][j] = puzzle[i][j]

    return copy_Puzz

def check_Status_File(puzzle):
    for i in range(3):
        for j in range(3):
            if str(puzzle[i][j]) > str(8):
                print("the File Numbering is Wrong. Please Upload Another File!!!")
                return False
            else:
                return True

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
        self.g_n = g_n
        self.h_n = h_n


    def add_Vertex(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)

    def goal_Check(self):
        # print_matrix(self.v_puzzle)
        goal_Mat = build_distination(3, 3)
        # print(goal_Mat)
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
        # print(puzz_R)
        # print("*******************")
        # puzz_R = self.v_puzzle
        # print(puzz_R)
        if self.col < 2:
            # print("Moving Right...")
            temp_R = puzz_R[self.row][self.col+1]
            puzz_R[self.row][self.col+1] = puzz_R[self.row][self.col]
            puzz_R[self.row][self.col] = temp_R
            return puzz_R

        else:
            # print("can't move Right! col = {0}".format(self.col))
            return False


        
    
    def move_Puzz_Up(self):
        # pass
        puzz_U = self.copy_Puzzle()
        # print(puzz_U)
        # print("*****************************")
        # puzz_U = self.v_puzzle
        # print(puzz_U)
        if self.row > 0:
            # print("Moving Up...")
            temp_U = puzz_U[self.row-1][self.col]
            puzz_U[self.row-1][self.col] = puzz_U[self.row][self.col]
            puzz_U[self.row][self.col] = temp_U
            return puzz_U

        else:
            # print("can't move Up! row = {0}".format(self.row))
            return False

    
    def move_Puzz_Down(self):
        # pass
        puzz_D = self.copy_Puzzle()
        # puzz_D = self.v_puzzle
        if self.row < 2:
            # print("Moving Down...")
            temp_D = puzz_D[self.row+1][self.col]
            puzz_D[self.row+1][self.col] = puzz_D[self.row][self.col]
            puzz_D[self.row][self.col] = temp_D
            return puzz_D
        
        else:
            # print("can't move Down! row = {0}".format(self.row))
            return False
    
    def move_Puzz_Left(self):
        # pass
        # puzz_L = [[0 for x in range(3)] for y in range(3)]
        puzz_L = self.copy_Puzzle()
        # puzz_L = self.v_puzzle
        if self.col > 0:
            # print("Moving Left...")
            temo_V = puzz_L[self.row][self.col-1]
            puzz_L[self.row][self.col-1] = puzz_L[self.row][self.col]
            puzz_L[self.row][self.col] = temo_V
            return puzz_L
        
        else:
            # print("can't move Left! col = {0}".format(self.col))
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


node_Creation_Counter = 0
expand = list()
class Tree:
    def __init__(self, puzzle, counter=0):
        global node_Creation_Counter
        self.main = Vertex(puzzle, counter)
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        node_Creation_Counter += 1

    def __lt__(self, other):
        # print("hello!!!")
        return self.main.g_n < other.main.g_n

    
    def BFS(self):

        counter = 0
        expand.append(self)
        print ('%s%s Processing ... %s' % (fg(1), attr('bold'), attr('reset')))
        while self.main.goal_Mode != True:
            counter += 1
            check = expand.pop(0)
            # print_matrix(check.main.v_puzzle)
            # print("***************************")
            # print("***************************")
            # print("***************************")

            check.main.goal_Mode = check.main.goal_Check()
            if check.main.goal_Mode == True:
                print ('%s%s Yue Have Finally Reached the Goal !!! %s' % (fg('red'), bg('cyan'), attr('reset')))
                print("the Answare id Equal with : ")
                print(check.main.v_name)
                print_matrix(check.main.v_puzzle)
                print("#################################")
                print("The number of the nodes that Created is equal with : {0}.".format(node_Creation_Counter))
                return "Success !!!"

            else:
                up_temp = check.main.move_Puzz_Up()
                down_temp = check.main.move_Puzz_Down()
                right_temp = check.main.move_Puzz_Right()
                left_temp = check.main.move_Puzz_Left()

                if up_temp != False:
                    # self.up = Vertex(up_temp, counter)
                    check.up = Tree(up_temp)
                    # self.up.parent = self.main
                    # self.main.neighbors.append(self.up)
                    # check.up.main.
                    # if self.up.goal_Mode == True:
                    #     return "Success!!!"
                    expand.append(check.up)
                    counter+=1

                if down_temp != False:
                    # self.down = Vertex(down_temp, counter)
                    check.down = Tree(down_temp)
                    # self.down.parent = self.main
                    # self.main.neighbors.append(self.down)
                    # if self.down.goal_Mode == True:
                    #     return "Success!!!"
                    expand.append(check.down)
                    counter+=1

                if left_temp != False:
                    # self.left = Vertex(left_temp, counter)
                    check.left = Tree(left_temp)
                    # self.left.parent = self.main
                    # self.main.neighbors.append(self.left)
                    # if self.left.goal_Mode == True:
                    #     return "Success!!!"
                    expand.append(check.left)
                    counter+=1

                if right_temp != False:
                    check.right = Tree(right_temp)
                    # self.right = Vertex(right_temp, counter)
                    # self.right.parent = self.main
                    # self.main.neighbors.append(self.right)
                    expand.append(check.right)
                    counter+=1
                    

    def UCS(self):
        priority_Q = Q.PriorityQueue()
        heap_q = []
        counter = 0
        heapq.heappush(heap_q, self)
        print ('%s%s Processing ... %s' % (fg(1), attr('bold'), attr('reset')))
        while self.main.goal_Mode != True:
            counter +=1
            check = heapq.heappop(heap_q)
            check.main.goal_Mode = check.main.goal_Check()
            if check.main.goal_Mode == True:
                print("We have finally reched the Goal!!!")
                print("the answare is equal with : ")
                print(check.main.v_name)
                print_matrix(check.main.v_puzzle)
                return "Success!!!"

            else:
                temp_up = check.main.move_Puzz_Up()
                temp_down = check.main.move_Puzz_Down()
                temp_left = check.main.move_Puzz_Left()
                temp_right = check.main.move_Puzz_Left()

                if temp_up != False:
                    # self.up = Vertex(self.main.move_Puzz_Up(), counter)
                    check.up = Tree(temp_up)
                    check.up.main.g_n += (1+check.main.g_n)

                    # self.up.g_n += (1 + self.main.g_n)
                    # self.up.parent = self.main
                    # self.main.neighbors.append(self.up)

                    heapq.heappush(heap_q, (check.up))
                    counter +=1
                
                if temp_down != False:
                    # self.down = Vertex(self.main.move_Puzz_Down(), counter)
                    check.down = Tree(temp_down)
                    check.down.main.g_n += (1+check.main.g_n)
                    # self.down.g_n += (1 + self.main.g_n)
                    # self.up.parent = self.main
                    # self.main.neighbors.append(self.down)
                    heapq.heappush(heap_q, check.down)
                    counter +=1

                if temp_left != False:
                    # self.left = Vertex(self.main.move_Puzz_Right(), counter)
                    check.left = Tree(temp_left)
                    check.main.g_n += (1+check.main.g_n)
                    # self.left.g_n += (1 + self.main.g_n)
                    # self.up.parent = self.main
                    # self.main.neighbors.append(self.left)
                    heapq.heappush(heap_q, check.left)
                    counter +=1

                if temp_right != False:
                    # self.right= Vertex(self.main.move_Puzz_Right(), counter)
                    check.right = Tree(temp_right)
                    check.main.g_n += (1+check.main.g_n)
                    # self.right.g_n += (1 + self.main.g_n)
                    # self.up.parent = self.main
                    # self.main.neighbors.append(self.right)
                    heapq.heappush(heap_q, check.right)
                    counter +=1


def file_Read():
    file_name = input("Enter name of your file : >>> ")
    print(file_name)
    file = ''
    try:
        file = open(file_name,"r")
    except :
        print("error in opening file")
        exit()

    # print("hey")
    # print(file)
    lines = file.readlines()
    print(lines)
    ar = []
    # print(len(lines))
    if(len(lines) != 3):
        print("you have Entered Wrong Puzzle the number of your Lines id : {0}.".format(len(lines)))
        print("this program is designed to solve 8-puzzle.")
        exit()
    else:
        for line in lines:
            line = line.replace("\n","")
            item = line.split(" ")           
            ar.append(item)
        # print(ar)
        status = check_Status_File(ar)
        if(status == False):
            print("error in input file values")
        else:
            puzz = build_distination(3, 3)
            for i in range(3):
                for j in range(3):
                    puzz[i][j] = int(ar[i][j])
            return puzz

def test_BFS(puzzle):
    # pass
    T = Tree(puzzle)
    s = T.BFS()
    # print(s)
    print(stylize("### Success ! ###", colored.fg("medium_orchid_1b")))
    # medium_orchid_1b


def test_UCS(puzzle):
    # pass
    T = Tree(puzzle)
    s = T.UCS()
    # print(s)
    print(stylize("### Success ! ###", colored.fg("medium_orchid_1b")))

def main():
    upload_option = 100
    choose = 100
    global puzzle
    while(upload_option != 0):
        print("#1 : Enter '1' if you want to Read From An File!")
        print("#2 : Enter '2' if you want to Run a Random Puzzle !")
        print("#3 : Handy Inputting!!! Enter >> '3' <<")
        print("#4 : Enter '0' if you want to Exit !")
        upload_option = input("Make your Choice >>> ")
        if upload_option == '1':
            ar = file_Read()
            puzzle = copy_Puzzle(ar)

            if puzzle == False:
                print("there Was a Error in the readed file plz Try again!!!")
                continue
            else:
                break
        if upload_option == '3':
            test = False
            mat = build_distination(3, 3)
            while test != True:
                for i in range(3):
                    for j in range(3):
                        mat[i][j] = int(input("Please Enter Puzlle[{0}][{1}] : >>>".format(i, j)))
                test = check_Status_File(mat)
                if test == False:
                    print("Error in your Inputs please Try again!")
                    ex = input("or if you want to try another way Enter >> 1 << : ")
                    if ex == '1':
                        break
                else:
                    puzzle = mat
                    break
            break

                


        if upload_option == '2':
            # pass
            continue
        if upload_option == '0':
            print("###*************###")
            print("Thanks For using our Program!!!")
            print("***Good Luck!***")
            exit()
        else:
            print("You made An out of Rnage Choice please Choose Again!!!")
            
    while(choose != 0):
        # print("#1 : Enter '1' if you want the BFS Algorithm !")
        print(stylize("#1 : Enter '1' if you want the BFS Algorithm !", colored.fg("dark_orange")))
        # print("#2 : Enter '2' if you want the USC Algorithm !")
        print(stylize("#2 : Enter '2' if you want the USC Algorithm !", colored.fg("green")))
        # print("#3 : Enter '0' if you want to Exit !")
        print ('%s%s #3 : Enter "0" if you want to Exit ! %s' % (fg(1), bg(15), attr(0)))
        choose = input("please Enter your choice >>> ")
        if choose == '1':
            # pass
            # print(puzzle)
            try:
                cProfile.run('test_BFS(puzzle)')
            except KeyboardInterrupt:
                print(stylize("You have Intrupted the Progress!!!", colored.fg("green")))

        if choose == '2':
            # pass
            try:
                cProfile.run('test_UCS(puzzle)')
            except KeyboardInterrupt:
                print(stylize("You have Intrupted the Progress!!!", colored.fg("green")))
        if choose == '0':
            print("###*************###")
            print("Thanks For using our Program!!!")
            print("***Good Luck!***")
            exit()
        else:
            print("you made a Wrong Choice!!! please Try again!!")

# T = Tree([[3,1,2],[0,4,5],[6,7,8]])
# # s = T.BFS()
# s = T.UCS()
# print(s)
main()