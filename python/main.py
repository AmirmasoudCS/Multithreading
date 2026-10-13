# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

import threading
import time


def walk_the_dog():
    print("You finish walking the dog.")

def take_out_trash():
    print("You take out the trash.")

def get_mail():
    print("You get the mail.")

