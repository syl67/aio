import datetime
import json

from aiohttp import web
from aiohttpdemo_polls import db

def to_serializable(val):
    if isinstance(val, datetime):
        return val.isoformat() + "Z"
    return str(val)

async def index(request):
    async with request.app['db'].acquire() as conn:
        cursor = await conn.execute(db.question.select())
        records = await cursor.fetchall()
        questions = [dict(q) for q in records]

        return web.json_response({"data": questions}, dumps=json.dumps)
