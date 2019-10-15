import asyncio
import websockets

async def response(websocket, path):
    message = await websocket.recv()
    print("We got message from client:", message)
    await websocket.send("I confirm I got your message")

start_server = websockets.serve(response, '0.0.0.0', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()