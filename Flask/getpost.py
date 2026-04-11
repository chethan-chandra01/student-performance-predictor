from flask import Flask,render_template,request



app=Flask(__name__)


@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/index",methods=['GET'])
def index():
    return "This is index page"

@app.route("/intro")
def intro():
    return "Hello !! :)"


@app.route('/form',methods=['GET','POST'])
def appli():
    if(request.method=='POST'):
        name=request.post







if __name__ =="__main__":
    app.run(debug=True)