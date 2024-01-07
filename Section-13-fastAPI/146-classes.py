import asyncio


async def suma_slow(n1, n2):
    await asyncio.sleep(4)
    print(n1 + n2)


async def resta_fast(n1, n2):
    print(n1 - n2)


async def main():
    task1 = asyncio.create_task(suma_slow(1, 2))
    task2 = asyncio.create_task(resta_fast(5, 4))

    await task1
    await task2


asyncio.run(main())