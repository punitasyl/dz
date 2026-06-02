import random
import asyncio
# Имитация отправки письма пользователю:


async def send_email(user: str) -> None:
    '''- ждёт случайное время от 0.3 до 0.8 секунд
       - печатает: "Email sent to {user}"
    '''
    await asyncio.sleep(0.3 + 0.5 * random.random())
    print(f"Email sent to {user}")

async def send_bulk(users: list[str]) -> None:
    '''Должна:
        - запустить send_email для каждого пользователя ПАРАЛЛЕЛЬНО
        - дождаться завершения всех отправок
    '''
    tasks = [asyncio.create_task(send_email(user)) for user in users]
    await asyncio.gather(*tasks)

async def main():
    users = ["alice", "bob", "charlie", "dave", "eve"]
    await send_bulk(users)

asyncio.run(main())