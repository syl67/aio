from aiohttp import web

from aiohttpdemo_polls.db import init_pg, close_pg
from aiohttpdemo_polls.routes import setup_routes
from aiohttpdemo_polls.settings import config

app = web.Application()
setup_routes(app)
app['config'] = config
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)
web.run_app(app)
