from flask import *
app=Flask(__name__)
@app.route("/")
def home():
      return "this is home page"
@app.route("/contact")
def contactfun():
    return "this is contact page"
app.run()
