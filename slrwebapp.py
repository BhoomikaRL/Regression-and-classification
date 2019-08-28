from flask import Flask,render_template,request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app=Flask(__name__,static_folder='public')


@app.route('/')
def index():
    x=np.arange(0,11,1)
    y=x**2
    plt.plot(x,y,'r-o')
    img=io.BytesIO()
    plt.savefig(img,format='png')
    graphUrl=base64.b64encode(img.getvalue()).decode()
    return render_template('index.html',graphInfo=graphUrl)



if __name__=='__main__':
    app.run(debug=True)
    

