from flask import Flask,render_template,request

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('new.html')
@app.route('/abc')
def abc():
    return"hey"

@app.route('/add',methods=["POST"])
def add():
    add=request.form['name']
    print(add)
    return "the sum is "+add
if __name__=='__main__':
    app.run(debug=True)
    

