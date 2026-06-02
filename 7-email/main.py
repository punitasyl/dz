

import asyncio

# async def get_message():
#     return "Hello, World!"

# async def main():
#     result = await asyncio.create_task(get_message())
#     print(result)
    
# asyncio.run(main())

import time

# async def fetch():
#     await asyncio.sleep(2)
#     return 'done'

# async def main():
#     tasks = [fetch() for _ in range(3)]
#     results = await asyncio.gather(*tasks)
#     print(results)



# asyncio.run(main())

import requests
import aiohttp

# async def main():
#     # res = requests.get('https://google.com', timeout=10)
#     # print(res.status_code)
#     async with aiohttp.ClientSession() as session:
#         res = await session.get('https://google.com')
#         print(res.status)

# asyncio.run(main())


async def save():
    print("Saving...")
    await asyncio.sleep(2)
    print("Saved")

async def job():
    print("Working...")
    t = asyncio.create_task(save())
    await asyncio.shield(t)
    await asyncio.sleep(5)
    print("Done")
    
async def main():
    task = asyncio.create_task(job())
    await asyncio.sleep(1)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print(task.cancelled())
        print("Task was cancelled")
    await asyncio.sleep(4)


asyncio.run(main())