import asyncio
import threading
import multiprocessing

async def async_logic():
    print("Async")
    print("Async End")

def thread_logic():
    print("Thread")
    asyncio.run(async_logic())
    print("Thread End")

def proc_logic():
    print("Process")
    threading.Thread(target=thread_logic).start()
    print("Process End")

if __name__ == "__main__":
    print("Code")
    proc = multiprocessing.Process(target=proc_logic)
    proc.start()
    proc.join()
    print("Code End")

