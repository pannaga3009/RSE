from flask import Flask, render_template, request
import tablib
from RSE import get_output
import os
import csv
app = Flask(__name__)

list = []
# open csv file
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

#initial landing page
@app.route("/")
def index():
   return render_template("index.html")

#initial landing page
@app.route("/all")
def all():
   return render_template("all.html", restaurant = get_output())

#on button click redirected page
@app.route('/result',methods = ['POST', 'GET'])
def result():

    if request.method == 'POST':
         if request.form['submit'] == 'page1':
            data = list[0][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page2':
            data = list[1][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page3':
            data = list[2][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page4':
            data = list[3][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page5':
            data = list[4][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page6':
            data = list[5][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page7':
            data = list[6][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page8':
            data = list[7][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page9':
            data = list[8][2]
            return render_template("index1.html",data=data)
         elif request.form['submit'] == 'page10':
            data = list[9][2]
            return render_template("index1.html",data=data)

if __name__ == '__main__':
   app.run(debug = True)
