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
    
    walk_the_dog()
    take_out_trash()
    get_mail()

if __name__ == "__main__":
    choice = int(input("What method to inspect?\n1.No Threading\n2.Yes Threading\n"))
    if choice == 1:
        no_threading()