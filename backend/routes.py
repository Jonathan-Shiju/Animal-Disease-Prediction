def setup_routes(app):
    @app.route('/')
    def index():
        return "<h1>Connected to text model backend</h1>"

    @app.route('/api/status')
    def status():
        return {"message": "API is running", "status": "success"}

