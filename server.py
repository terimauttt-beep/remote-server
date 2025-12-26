import asyncio
import websockets

async def handler(websocket):
    print("Client connected")
    try:
        while True:
            cmd = input("Enter command (VIBRATE/RING): ")
            await websocket.send(cmd)
    except websockets.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 10000):
        print("WebSocket server running")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

