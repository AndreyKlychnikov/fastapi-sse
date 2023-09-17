import datetime
import json
import uuid
from typing import Iterable

import asyncio
from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
async def read_index():
    return FileResponse("index.html")


STREAM_DELAY = 1  # second
RETRY_TIMEOUT = 15000  # millisecond


def get_new_messages() -> Iterable:
    return [
        {
            "event": "new_message",
            "retry": RETRY_TIMEOUT,
            "data": json.dumps(
                {
                    "message": "test message",
                    "datetime": datetime.datetime.now().isoformat(
                        sep="T", timespec="auto"
                    ),
                }
            ),
            "id": uuid.uuid4(),
        }
    ]


async def event_generator(request: Request):
    while True:
        if await request.is_disconnected():
            break
        for message in get_new_messages():
            yield message
        await asyncio.sleep(STREAM_DELAY)


@app.get("/stream")
async def message_stream(request: Request):
    return EventSourceResponse(event_generator(request))
