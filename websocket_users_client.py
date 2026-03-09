import asyncio

import websockets

async def user_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(f"Отправка сообщения: {message}")
        await websocket.send(message)

        for _ in range(5):
            response = await websocket.recv()
            print("Получения сообщения: ", response)


asyncio.run(user_client())