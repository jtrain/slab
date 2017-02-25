import bottle

from demo.routes import Routes as DemoRoutes
from core.routes import Routes as CoreRoutes

app = bottle.default_app()
app.merge(CoreRoutes)
app.merge(DemoRoutes)

app.config.load_config('config/settings.ini')


bottle.run(reloader=True)
