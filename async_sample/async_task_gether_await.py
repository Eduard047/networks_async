import asyncio

async def loop1():
    counter = 0
    while True:
        counter += 1
        print(f"Loop one: {counter}")
        await asyncio.sleep(1)

async def loop2():
    counter = 0
    while True:
        counter += 1
        print(f"Loop two: {counter}")
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(loop1())
    task2 = asyncio.create_task(loop2())
    #await loop1()
    #await loop2()
    await asyncio.gather(task1, task2)

asyncio.run(main())
#coroutine = loop1()
#print(coroutine)
#print(type(coroutine))

