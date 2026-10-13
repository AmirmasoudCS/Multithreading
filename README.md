# Multithreading

A simple Python project demonstrating the difference between sequential execution and multithreading using everyday tasks.

## What Is Multithreading?

Multithreading allows multiple threads to execute concurrently within the same process. It is particularly useful for I/O-bound tasks, such as reading files or making API requests, where threads can make progress while other tasks wait.

In this project, three chores take different amounts of time. The program compares executing them sequentially with running them concurrently using threads.

## Creating Threads in Python

Python's built-in `threading` module provides the `Thread` class.

```python
import threading

thread = threading.Thread(target=my_function)
thread.start()
thread.join()
```

- `target`: The function the thread will execute. Pass the function itself, without parentheses.
- `start()`: Starts the thread.
- `join()`: Waits for the thread to finish.

## Running the Project

```bash
python main.py
```

Choose between sequential execution and multithreading to compare their execution times.