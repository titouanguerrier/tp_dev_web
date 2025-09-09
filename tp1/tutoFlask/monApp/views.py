from .app import app

@app.route('/')
def index( ) :
    return "Hello world !"
@app.route('/about')
def about():
    return app.config['ABOUT']
if __name__== "__main__" :
    app.run( )

