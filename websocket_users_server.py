import asyncio

import websockets
from websockets import ServerConnection


async def user_service(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")
        response = f"Сообщение пользователя: {message}"

        for _ in range(5):
            await websocket.send(response)


async def main():
    server = await websockets.serve(user_service, "localhost", 8765)
    print("Сервер стартует на  ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())


