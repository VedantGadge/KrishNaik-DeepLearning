from flask import Flask, render_template , request

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

@app.route('/form',methods=['GET','POST'])
def form():
    if request.method=='POST':
        name = request.form['name']
        return f'<h1>Welcome {name}!<h1>'
    return render_template('form.html')

###Jinja 2 template

@app.route('/success/<int:score>') ## we are giving some rule to the parameter , this is known as variable ruling
def success(score):
    res =""
    if score>=50:
        res = "PASSED"
    else:
        res = "FAILED"
    
    return render_template('results.html',results = res)
        
        


# Entry point of this application (app.py)
if __name__ == '__main__':
    app.run(debug=True)

