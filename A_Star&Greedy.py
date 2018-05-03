import heapq
from colored import fg, bg, attr
from copy import deepcopy
# from colored import fg, bg, attr
import cProfile
import colored
from colored import stylize
# import timeit
# import sys
# sys.setrecursionlimit(3500)
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

xxx = build_distination(3, 3)

def copy_Puzzle(puzzle):
    copy_Puzz = [[0 for i in range(3)] for j in range(3)]
    for i in range(3):
        for j in range(3):
            # print("helooo")
            copy_Puzz[i][j] = puzzle[i][j]

    return copy_Puzz


def print_matrix(array_list):
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) for row in array_list]))

def find_Address(puzzle3, row, col):
    # the_num_have_to_be = (row * 3) + col
    count = 0
    for i in range(3):
        for j in range(3):
            if puzzle3 == xxx[i][j]:
                temp = (abs(i - row) + abs(j - col))
                count += temp
                # print(count)
                return count

def check_Status_File(puzzle):
    for i in range(3):
        for j in range(3):
            if str(puzzle[i][j]) > str(8):
                print("the File Numbering is Wrong. Please Upload Another File!!!")
                return False
            else:
                return True

def find_Empty_Row_Col(Matrix):
    # print_matrix(Matrix)

    for i in range(int(3)):
        for j in range(int(3)):
            # print("helooo")
            # print(Matrix[i][j])
            if Matrix[i][j] == 0:
                return j,i

def count_H_N(puzzle):
    sum_1 = 0
    puzz_count = 0
    i_count = 0
    j_count = 0
    for i in range(3):
        for j in range(3):
            if puzzle[i][j] != puzz_count:

                temp = find_Address(puzzle[i][j], i, j)
                # i_count = int(int(puzzle[i][j]) / int(3))
                # j_count = int(int(puzzle[i][j]) % int(3))

                # temp = int(abs(int(i) - int(i_count)) + abs(int(j) - int(j_count)))
                sum_1 += temp
            puzz_count+=1
            # j_count+=1
        # i_count+=1
            
    return sum_1


def count_H_N_2(puzzle):
    col_address, row_address = find_Empty_Row_Col(puzzle)
    diff = col_address + row_address + 2
    return diff


class Vertex:
    def __init__(self, puzzle, name, g_n=0, h_n=0, parent=None):
        self.v_name = name
        self.v_puzzle = puzzle
        self.goal_Mode = self.goal_Check()
        # self.color = 'Black'
        # self.parent = parent
        # self.neighbours = list()
        # print("####################################")
        # print_matrix(self.v_puzzle)
        self.col, self.row = find_Empty_Row_Col(self.v_puzzle)
        self.g_n = g_n
        self.h_n = h_n
        self.f_n = self.g_n + self.h_n


###################*********    An Module For checking are we in Goal that we want or Not    *********######################
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
            return self.goal_Mode

        # else:
        #     com_mat = [[2,1,0],[5,4,3],[8,7,6]]
        #     for i in range(3):
        #         for j in range(3):
        #             if self.v_puzzle[i][j] == com_mat[i][j]:
        #                 self.goal_Mode = True
        #             else:
        #                 self.goal_Mode = False
        #                 return self.goal_Mode
                    
        # return self.goal_Mode

###################*******   An module For Copying the current Puzzle    *******#############
    def copy_Puzzle(self):
        copy_Puzz = [[0 for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                copy_Puzz[i][j] = self.v_puzzle[i][j]

        return copy_Puzz

##############################################******   Moving Part    ******##############################################
    def move_Puzzle_Right(self):
        # puzz_R = self.
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
        # puzz_U = self.copy_Puzzle()
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
        # puzz_D = self.copy_Puzzle()
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
        # puzz_L = self.copy_Puzzle()
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

##########################################*******   End Moving Part   *******############################################


    def __str__(self):
        return self.v_name



priority_Queue = []
node_Creation_Counter = 0

####################********    Tree Class    *******##################
class Tree:
    def __init__(self, puzzle, counter = 0):
        global node_Creation_Counter
        # global breth_counter
        self.main = Vertex(puzzle, counter)
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.parent = self
        node_Creation_Counter += 1
        
        

    def A_Star(self, a_star):
        # global node_Creation_Counter
        st = Tree(self.main.v_puzzle)
        counter_main = 0
        counter = 0
        print ('%s%s Processing ... %s' % (fg(1), attr('bold'), attr('reset')))
        counter = 0
        self.parent = None
        heapq.heappush(priority_Queue, self)
        # print_matrix(self.main.v_puzzle)
        # lisewe = list()
        while self.main.goal_Mode != True:
            # counter += 1
            # heapq.heapify(priority_Queue)
            check = heapq.heappop(priority_Queue)
            # print("#########################################")
            # print_matrix(check.main.v_puzzle)
            # print("#########################################")
            # lisewe.append(check.main.v_puzzle)
            # print_matrix(check.main.v_puzzle)
            # counter_main += 1
            check.main.goal_Mode = check.main.goal_Check()
            if check.main.goal_Mode == True:
                # print("Yue Have Finally Reached the Goal !!!")
                print ('%s%s Yue Have Finally Reached the Goal !!! %s' % (fg('red'), bg('cyan'), attr('reset')))
                print("the Answare id Equal with : ")
                print(check.main.v_name)
                print_matrix(check.main.v_puzzle)
                print("#################################")
                print("The number of the nodes that Created is equal with : {0}.".format(node_Creation_Counter))
                print(self.counter(check))
                # print_matrix(check.parent.parent.main.v_puzzle)
                return "Success !!!"
            else:
                up_temp = check.main.move_Puzzle_Up()
                down_temp = check.main.move_Puzzle_Down()
                left_temp = check.main.move_Puzzle_Left()
                right_temp = check.main.move_Puzzle_Right()
                if up_temp != False:
                    check.up = Tree(up_temp)
                    check.up.main.v_puzzle = up_temp
                    # Vertex(self.main.move_Puzzle_Up(), counter)
                    h_n_up = count_H_N(check.up.main.v_puzzle)
                    check.up.main.h_n = h_n_up
                    if (a_star == True):
                        check.up.main.g_n += (1+check.main.g_n)
                    if (a_star == False):
                        check.up.main.g_n = 0
                    # print("fdggffd")
                    check.up.main.f_n = check.up.main.h_n + check.up.main.g_n
                    # self.up.main.parent = self.main
                    # tc.parent = check
                    check.up.parent = check
                    # st.up = Tree(up_temp)
                    # st.parent = check
                    # check.up.parent.main.v_puzzle = check.main.v_puzzle
                    heapq.heappush(priority_Queue, check.up)
                    
                    # print_matrix(check.up.parent.main.v_puzzle)
                    # node_Creation_Counter += 1

                    counter+=1
                    
                if down_temp != False:
                    check.down = Tree(down_temp)
                    check.down.main.v_puzzle = down_temp
                    # Vertex(self.main.move_Puzzle_Down(), counter)
                    h_n_down = count_H_N(check.down.main.v_puzzle)
                    check.down.main.h_n = h_n_down
                    if (a_star == True):
                        check.down.main.g_n += (1+check.main.g_n)
                    if (a_star == False):
                        check.down.main.g_n = 0

                    check.down.main.f_n = check.down.main.h_n + check.down.main.g_n
                    # self.down.main.parent = self.main
                    check.down.parent = check
                    # st.down = Tree(down_temp)
                    # st.parent = check
                    # check.down.parent.main.v_puzzle = check.main.v_puzzle
                    heapq.heappush(priority_Queue, check.down)
                    # node_Creation_Counter += 1
                    
                    # print_matrix(check.up.parent.main.v_puzzle)

                    counter+=1
                
                if left_temp != False:
                    check.left = Tree(left_temp)
                    check.left.main.v_puzzle = left_temp
                    # Vertex(self.main.move_Puzzle_Left(), counter)
                    h_n_left = count_H_N(check.left.main.v_puzzle)
                    check.left.main.h_n = h_n_left
                    if (a_star == True):
                        check.left.main.g_n += (1+check.main.g_n)
                    if (a_star == False):
                        check.left.main.g_n = 0

                    check.left.main.f_n = check.left.main.h_n + check.left.main.g_n
                    # self.left.main.parent = self.main
                    check.left.parent = check
                    # st.left = Tree(left_temp)
                    # st.parent = check
                    # check.left.parent.main.v_puzzle = check.main.v_puzzle
                    # print_matrix(check.main.v_puzzle)
                    heapq.heappush(priority_Queue, check.left)
                    # node_Creation_Counter += 1
                    
                    # print_matrix(check.up.parent.main.v_puzzle)

                    counter+=1

                if right_temp != False:
                    check.right = Tree(right_temp)
                    check.right.main.v_puzzle = right_temp
                    # Vertex(self.main.move_Puzzle_Right(), counter)
                    h_n_right = count_H_N(check.right.main.v_puzzle)
                    check.right.main.h_n = h_n_right
                    if (a_star == True):
                        check.right.main.g_n += (1+check.main.g_n)
                    if (a_star == False):
                        check.right.main.g_n = 0

                    check.right.main.f_n = check.right.main.h_n + check.right.main.g_n
                    # self.right.main.parent = self.main
                    check.right.parent = check
                    # st.right = Tree(right_temp)
                    # st.parent = check
                    # check.right.parent.main.v_puzzle = check.main.v_puzzle
                    heapq.heappush(priority_Queue, check.right)
                    # node_Creation_Counter += 1
                    
                    # print_matrix(check.up.parent.main.v_puzzle)

                    counter+=1
            
            
                # dsff = [[0 for i in range(3)] for j in range(3)]
                # T = Tree(dsff)
                # self = T.main = check

    def counter(self, node):
        breth_counter = 1
        # print_matrix(node.parent.main.v_puzzle)
        while node.parent != None:
            # self.breth_counter+=1
            # print(node)
            # print(node.parent)
            print("$$$$$$$$$$$$$************$$$$$$$$$$$$$$$$$")
            print_matrix(node.main.v_puzzle)
            print("$$$$$$$$$$$$$************$$$$$$$$$$$$$$$$$")
            node = node.parent
            # print()
            breth_counter+=1
        # print(lisew)
        return breth_counter

    def __lt__(self, other):
        # print("hello!!!")
        return int(self.main.f_n) < int(other.main.f_n)



# T = Tree([[7,2,4],[5,0,6],[8,3,1]])
# s = A_Star(T)
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
    # print(lines)
    ar = []
    # print(len(lines))
    if(len(lines) != 3):
        print("you have Entered Wrong Puzzle the number of your Lines id : {0}.".format(len(lines)))
        print("this program is designed to solve 8-puzzle.")
        return False
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

# puzzle = 0
# puzz = [[7,2,4],[5,0,6],[8,3,1]]

def test_A_Star(puzzle):
    # print_matrix(puzzle)
    T = Tree(puzzle)
    s = T.A_Star(True)
    # print(s)
    print(stylize("### Success ! ###", colored.fg("medium_orchid_1b")))

def test_Greedy(puzzle):
    k = Tree(puzzle)
    s = k.A_Star(False)
    print(s)
    print(stylize("### Success ! ###", colored.fg("medium_orchid_1b")))

import cProfile

def main():
    upload_option = 100
    choose = 100
    # global puzzle
    # puzzle = 0
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
            # print_matrix(puzzle)
            if puzzle == False:
                print("there Was a Error in the readed file plz Try again!!!")
                continue
            else:
                break

        if upload_option == '2':
            # pass
            continue

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

        if upload_option == '0':
            print("###*************###")
            print("Thanks For using our Program!!!")
            print("***Good Luck!***")
            exit()
        else:
            print("You made An out of Rnage Choice please Choose Again!!!")
            
    while(choose != 0):
        print("#1 : Enter '1' if you want the A* Algorithm !")
        print("#2 : Enter '2' if you want the Greedy Algorithm !")
        print("#3 : Enter '0' if you want to Exit !")
        choose = input("please Enter your choice >>> ")
        if choose == '1':
            # pass
            # print(puzzle)
            try:
                cProfile.run('test_A_Star(puzzle)')

            except KeyboardInterrupt:
                print(stylize("You have Intrupted the Progress!!!", colored.fg("green")))
            
        if choose == '2':
            # pass
            try:
                cProfile.run('test_Greedy(puzzle)')
            except KeyboardInterrupt:
                print(stylize("You have Intrupted the Progress!!!", colored.fg("green")))

        if choose == '0':
            print("###*************###")
            print("Thanks For using our Program!!!")
            print("***Good Luck!***")
            exit()
        else:
            print("you made a Wrong Choice!!! please Try again!!")


# T = Tree([[7,2,4],[5,0,6],[8,3,1]])
# s = T.A_Star()
# print(s)
main()

# file_Read()

# import timeit
# print(timeit.timeit('[func() for func in (test)]', globals=globals()))
# import re
# cProfile.run('test()')
# if __name__ == '__main__':
#     import timeit
#     print(timeit.timeit("test()", setup="from __main__ import test"))


# t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')

# print(t)

