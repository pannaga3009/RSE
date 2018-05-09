from flask import Flask, render_template, request
import tablib
import os
import csv
app = Flask(__name__)
# dataset = tablib.Dataset()
# with open(os.path.join(os.path.dirname(__file__),'summary.csv')) as f:
#     dataset.csv = f.read()
list = []
# open file
with open('summary.csv', 'r') as f:
    reader = csv.reader(f)

    # read file row by row
    rowNr = 0
    for row in reader:
        # Skip the header row.
        if rowNr >= 1:
            list.append(row)
        # Increase the row number
        rowNr = rowNr + 1

@app.route("/")
def index():
   return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():

    if request.method == 'POST':
         if request.form['submit'] == 'page1':
            data = list[0][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page2':
            data = list[1][2]
            return render_template("index1.html",data=data)


if __name__ == '__main__':
   app.run(debug = True)
