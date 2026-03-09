import asyncio

import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Got message: {message}")
        response = f"Server got: {message}"

        for _ in range(5):
            await websocket.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("Server started on ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())