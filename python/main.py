# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

import threading
import time


def walk_the_dog():
    time.sleep(8)
    print("You finish walking the dog.")

def take_out_trash():
    time.sleep(2)
    print("You take out the trash.")

def get_mail():
    time.sleep(4)
    print("You get the mail.")

def no_threading():

    # Running on the same thread -> Sequentially
    
    walk_the_dog()
    take_out_trash()
    get_mail()

def yes_threading():

    # Running on different threads -> Parallel

    chore1 = threading.Thread(target=walk_the_dog)
    chore1.start()

    chore2 = threading.Thread(target=take_out_trash)
    chore2.start()

    chore3 = threading.Thread(target=get_mail)
    chore3.start()



if __name__ == "__main__":
    choice = int(input("What method to inspect?\n1.No Threading\n2.Yes Threading\n"))
    if choice == 1:
        no_threading()
    elif choice == 2:
        yes_threading()