#Multiprocess Example Basic

import multiprocessing

def p_square(num):
    print("Process1 Square => ",num*num)

def p_cube(num):
    print("Process2 Cube=> ",num*num*num)

#Protects Unexpected Run when importing this file to another file
if __name__ == "__main__":
    p1 = multiprocessing.Process(target=p_square,args=(2,))
    p2 = multiprocessing.Process(target=p_cube,args=(3,))

    print("Process Started")

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Done!");