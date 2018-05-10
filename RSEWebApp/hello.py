from flask import Flask, render_template, request
app = Flask(__name__)

from RSE import get_output

@app.route("/test")
def test():
   return render_template("test.html", restaurant=get_output())



@app.route("/")
def index():
   return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
       return render_template("index1.html")

if __name__ == '__main__':
   app.run(debug = True)
