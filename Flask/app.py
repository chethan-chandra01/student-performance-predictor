from flask import Flask,render_template,request



app=Flask(__name__)


@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/index")
def index():
    return "This is index page"

@app.route("/intro")
def intro():
    return "Hello !! :)"

@app.route("/form",methods=['GET','POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        phone=request.form['phone']
        return f'Hello{name}, your email Id is {email}and your phone number is {phone}'
    
    return render_template('form.html')







if __name__ =="__main__":
    app.run(debug=True)