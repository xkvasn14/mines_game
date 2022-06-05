# author: Jaroslav Kvasnička
import os
import random
import time
import math

mine = -1
show_distance = 2
size_x = -1
size_y = -1
mine_field_compute = []
mine_field = []
debug_mode = 1

def clear():
    clear = "cls"
    if(os.name == "posix"):
        clear = "clear"
    os.system(clear)
    return

def introduction():
    print("\033[1;33;40mWelcome to MINES!\033[0;37;10m")
    time.sleep(1.3)
    clear()
    print("\033[1;37;40mYour tasks:")
    time.sleep(1)
    print("Set up your game")
    time.sleep(1)
    print("Find all free spots")
    time.sleep(1)
    print("Don't step in a mine!\033[0;37;10m")
    input("continue by hitting \"Enter\":")
    clear()
    return

def user_input_validation():
    debug_mode = bool(input("Hit \"Enter\" if you want to continue without debug mode:"))
    if(debug_mode):
        print("You have chosen debug mode")
    
    while True:
        difficulty = input("Type in level of difficulty:\n"+"\033[1;32;40measy\n"+"\033[1;33;40mmedium\n"+"\033[1;31;40mhard\n"+"\033[1;35;40mimpossible\033[0;37;40m\n")
        clear()
        if(difficulty == "easy"):
            print("You have chosen \033[1;32;40measy\033[0;37;40m")
            show_distance = 3
            break
        elif(difficulty == "medium"):
            print("You have chosen \033[1;33;40mmedium\033[0;37;40m")
            show_distance = 2
            break
        elif(difficulty == "hard"):
            print("You have chosen \033[1;31;40mhard\033[0;37;40m")
            show_distance = 1
            break
        elif(difficulty == "impossible"):
            print("You have chosen \033[1;35;40mimpossible\033[0;37;40m")
            show_distance = 0
            break
        else:
            clear()

    while True:
        x_coord = input("Enter number of rows: ")
        clear()
        if(x_coord.isdigit()):
            if(int(x_coord) == 0):
                print("Please enter number bigger then 0")
            else:
                print("You have entered \033[1;32;40m" + x_coord + "\033[0;37;40m")
                break
        else:
            print("Please enter whole number!")
        
    while True:
        y_coord = input("Enter number of columns: ")
        clear()
        if(y_coord.isdigit()):
            if(int(y_coord) == 0):
                print("Please enter number bigger then 0")
            else:
                print("You have entered \033[1;32;40m" + y_coord + "\033[0;37;40m")
                break
        else:
            print("Please enter whole number!")
    
    while True:
        m_count = input("Enter number of mines: ")
        clear()
        if(m_count.isdigit()):
            print("You have entered \033[1;31;40m" + m_count + "\033[0;37;40m")
            if((int(y_coord) * int(x_coord)) < int(m_count)):
                print("You have entered more mines then are possible fields!")
                print("Maximum number of mines possible: ",(int(y_coord)*int(x_coord)))
            else:
                break
        else:
            print("Please enter whole number!")

    print("Your game will begin in...")
    time.sleep(0.75)
    print("3")
    time.sleep(0.75)
    print("2")
    time.sleep(0.75)
    print("1")
    time.sleep(0.75)
    return int(x_coord),int(y_coord),int(m_count), show_distance, debug_mode

def map_generator():
    minefield_chance = []
    for x in range(0,size_x):
        rows = []
        rowss = []
        for y in range(0,size_y):
            rows.append(random.random())
            rowss.append(" ")
        minefield_chance.append(rows)
        mine_field.append(rowss)

    mine_positions = []
    for m in range(0,m_count):
        rows = []
        for j in range(0,2):
            rows.append(0)
        mine_positions.append(rows)
    the_biggest_chance = [0 for x in range(0,m_count)]

    for m in range(0,m_count):
        for x in range(0,size_x):
            for y in range(0,size_y):
                    if(the_biggest_chance[m] < minefield_chance[x][y] and not minefield_chance[x][y] in the_biggest_chance):
                        the_biggest_chance[m] = minefield_chance[x][y]
                        mine_positions[m][0] = x
                        mine_positions[m][1] = y
    
    for x in range(0,size_x):
        rows = []
        for y in range(0,size_y):
            if(minefield_chance[x][y] in the_biggest_chance):
                rows.append(mine)
            else:
                rows.append(0)
        mine_field_compute.append(rows)
    
    for m in range(0,m_count):
        for x in range(0,size_x):
            for y in range(0,size_y):
                distance = int(math.sqrt((mine_positions[m][0] - x)**2 + (mine_positions[m][1] - y)**2))
                if(distance <= mine_field_compute[x][y] or mine_field_compute[x][y] == 0):
                    mine_field_compute[x][y] = distance

    return 

def text_color(number):
    text = ""
    if(not number.isdigit()):
        text = str(number)
    else:
        if(int(number) < 6):
            text = "\033[0;" + str(int(number) + 30) + ";40m " + str(number) + " \033[0;37;40m"
        elif(int(number) >= 6):
            text = "\033[0;35;40m " + str(number) + " \033[0;37;40m"
        else:
            text = str(number)
    return text

def map_show():
    clear()
    row = 0
    col = 0
    map = "\t\t"
    for i in range(0,size_y):
        map += "c" + str(i) + "\t|\t"
    for i in mine_field:
        map += "\n" + "r" + str(row) + "\t|\t"
        row += 1
        for j in i:
            map = map + text_color(str(j)) +  "\t|\t" 
            #map = map + str(j) + "\t|\t"
            col += 1
    print(map)

    if(debug_mode):
        row = 0
        col = 0
        map = "\t\t"
        for i in range(0,size_y):
            map += "c" + str(i) + "\t|\t"
        for i in mine_field_compute:
            map += "\n" + "r" + str(row) + "\t|\t"
            row += 1
            for j in i:
                map = map + text_color(str(j)) +  "\t|\t" 
                #map = map + str(j) + "\t|\t"
                col += 1
        print(map)

    return

def user_input():
    while True:
        x_coord = input("Enter row number: ")
        map_show()
        if(x_coord.isdigit()):
            print("You have entered " + x_coord)
            if(int(x_coord) > size_x -1 ):
                print("Please enter positive number smaller than",size_x)
            else:
                break
        else:
            print("Please enter whole number!")
    
    while True:
        y_coord = input("Enter column number: ")
        map_show()
        if(y_coord.isdigit()):
            print("You have entered " + y_coord)
            if(int(y_coord) > size_y -1 ):
                print("Please enter positive number smaller than",size_y)
            else:
                break
        else:
            print("Please enter whole number!")
    
    return int(x_coord),int(y_coord)

def distance_determination(row,col,show_distance):
    for x in range(0,size_x):
        for y in range(0,size_y):
            distance = int(math.sqrt((x - row)**2 + (y - col)**2))
            if(distance <= show_distance and mine_field_compute[x][y] != -1):
                mine_field[x][y] = str(mine_field_compute[x][y])

    return
    
def win_situation():
    for x in range(0,size_x):
        for y in range(0,size_y):
            if(mine_field[x][y] == " "):
                if(mine_field_compute[x][y] == -1):
                    pass
                else:
                    return True
            else:
                #if(int(mine_field[x][y]) == mine_field_compute[x][y]):
                pass

    clear()
    row = 0
    col = 0
    map = "\t\t"
    for i in range(0,size_y):
        map += "c" + str(i) + "\t|\t"
    for i in mine_field_compute:
        map += "\n" + "r" + str(row) + "\t|\t"
        row += 1
        col = 0
        for j in i:
            if(mine_field_compute[row-1][col] == mine):
                map = map + " \033[1;31;40mX\033[0;37;40m " +  "\t|\t" 
            else:
                map = map + text_color(str(j)) +  "\t|\t" 
            #map = map + str(j) + "\t|\t"
            col += 1
    print(map)
    print("\033[1;33;40mYou won! \033[0;37;40m")      
    return False

def map_mine_validation(row,col):
    if(mine_field_compute[row][col] == mine):
        mine_field[row][col] = " \033[1;31;40mX\033[0;37;40m "
        map_show()
        print("\033[1;31;40mYou hit a mine! \033[0;37;40m")
        return False
    else:
        distance_determination(row,col,show_distance)
        return win_situation()
    
def player_play():
    while True:
        map_show()
        row,col = user_input()
        if(map_mine_validation(row,col)):
            continue
        else:
            return
        
if __name__ == "__main__":
    clear()
    introduction()
    size_x, size_y, m_count, show_distance, debug_mode = user_input_validation()
    map_generator()
    map_show()
    player_play()
