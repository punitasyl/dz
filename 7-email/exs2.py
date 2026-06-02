import asyncio
import random

async def unstable():
    await asyncio.sleep(0.2)
    if random.random() < 0.5:
        raise Exception("Something went wrong")
    return "Success"



async def run_with_retry(job, max_retries=3):
    for _ in range(1, max_retries + 1):
        task = asyncio.create_task(job())
        try:
            result = await task
            print(f"Попытка {_}: Успех -> {result}")
            return result
        except Exception as e:
            print(f"Попытка {_}: Ошибка -> {e}")

            if _ == max_retries:
                print("Макс. кол-во попыток исчерпано")
                return "ERROR" 
            await asyncio.sleep(0.5)

async def main():
    # run_with_retry - сделать корутину, которая запустить корутину
    # если она выбросила ошибку, пробует заново до указанного лимита
    try:
        result = await run_with_retry(unstable)
        print(result)
    except Exception as e:
        print(f"Final error: {e}")



asyncio.run(main())