import asyncio
import threading
import multiprocessing

from proc_logic_module import proc_logic

def thread_logic():
    print("Thread")
    multiprocessing.Process(target=proc_logic, args=()).start()
    print("Thread End")

def async_logic():
    print("Async")
    multiprocessing.Process(target=proc_logic, args=()).start()
    print("Async End")

if __name__ == '__main__':
    print("Code")
    asyncio.run(async_logic())
    print("Code End")