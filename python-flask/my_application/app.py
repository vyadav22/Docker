from flask import Flask
from flask import request
import os, sys
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

#got the code from google 
@app.route("/files")
def list_files():
  path = "./uploads/"
  dirs = os.listdir(path)
  files = ""
  for file in dirs:
      files = str(files + file + ", ")
  return files

@app.route("/euler1")
def euler1():
  sum = 0
  for i in range (1, 1000):
    if i%3 or i%5:
      sum = sum + i
  return ("Euler 1:The total is ",sum)


@app.route("/euler2")
def euler2():
  t1 = 1
  t2 = 2
  total = 0
  sum = 2
  while(total < 4000000):
    total = t1 + t2
    t1 = t2
    term2 = total
    if(total%2 = 0):
      sum = sum  +total
  return("Euler 2: The total is ",sum)