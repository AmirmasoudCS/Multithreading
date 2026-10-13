import threading
import time


def walk_the_dog(name):
    start_time = time.perf_counter()
    time.sleep(8)
    elapsed_time = time.perf_counter() - start_time
    print(f"You finish walking {name}. Time taken: {elapsed_time:.2f} seconds.")

def take_out_trash():
    start_time = time.perf_counter()
    time.sleep(2)
    elapsed_time = time.perf_counter() - start_time
    print(f"You take out the trash. Time taken: {elapsed_time:.2f} seconds.")

def get_mail():
    start_time = time.perf_counter()
    time.sleep(4)
    elapsed_time = time.perf_counter() - start_time
    print(f"You get the mail. Time taken: {elapsed_time:.2f} seconds.")


def no_threading():
    start_time = time.perf_counter()
    # Running on the same thread -> Sequentially
    walk_the_dog("Torob")
    take_out_trash()
    get_mail()
    elapsed_time = time.perf_counter() - start_time
    print(f"Time took to do all the chores:\t{elapsed_time:.2f} seconds.")


def yes_threading():
    start_time = time.perf_counter()
    # Running on different threads -> Concurrently
    chore1 = threading.Thread(target=walk_the_dog, args=("Torob",))
    chore2 = threading.Thread(target=take_out_trash)
    chore3 = threading.Thread(target=get_mail)

    chore1.start()
    chore2.start()
    chore3.start()

    chore1.join()
    chore2.join()
    chore3.join()

    elapsed_time = time.perf_counter() - start_time
    print(f"Time took to do all the chores:\t{elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    choice = int(input("What method to inspect?\n1. No Threading\n2. Yes Threading\n"))

    if choice == 1:
        no_threading()
    elif choice == 2:
        yes_threading()