import bottle

app = bottle.default_app()
app.config.load_config('config/settings.ini')

bottle.run()
