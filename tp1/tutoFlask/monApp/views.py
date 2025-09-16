from .app import app
from flask import render_template

@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html",title ="R3.01 Dev Web avec Flask",name="Cricri")

@app.route('/about/')
def about():
    return render_template("about.html",title ="about",name=app.config['ABOUT'])

@app.route('/contact/')
def contact():
    return render_template("contact.html",title ="contact ",name=app.config['CONTACT'])
if __name__== "__main__" :
    app.run( )
