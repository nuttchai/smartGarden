import asyncio
import websockets

async def message():
    async with websockets.connect('ws://127.0.0.1:5678') as websocket:
        msg = input("What do you want to send: ")
        await websocket.send(msg)
        print(await websocket.recv())
        

asyncio.get_event_loop().run_until_complete(message())
#asyncio.get_event_loop().run_forever()