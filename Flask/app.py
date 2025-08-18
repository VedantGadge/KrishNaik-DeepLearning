from flask import Flask, render_template

'''
This will create a an instance of the Flask class,
which will be our WSGI (Web Server Gateway Interference) application
'''
app = Flask(__name__)

@app.route("/") ## Decorator fn to set up route
def welcome():
    return "Welcome to Flask!"

@app.route("/index")
def index():
    return render_template('index.html') # This will find the folder named 'templates' folder and find the given file



# Entry point of this application (app.py)
if __name__ == '__main__':
    app.run(debug=True)

