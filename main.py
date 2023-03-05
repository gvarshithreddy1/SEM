from flask import Flask, render_template
from calculation import calculation
from sem_methods import *
import random
import json

calculation("studentlist.txt")
roll_name_map("studentlist.txt", "allotment_results.txt")

app = Flask(__name__)

linebyline = []
filename = open("final_allotment.txt")
for line in filename:
  linebyline.append(line)
  

    

@app.route('/')
def index():
    return render_template('index.html', content = linebyline)



if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)