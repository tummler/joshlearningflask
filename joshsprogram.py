"""
Made a dumb website
"""
from flask import Flask, request, render_template
import requests
app = Flask(__name__)
app.debug = True

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/poop")
def poop():
	return "You have poop in your pants"

@app.route("/getpoop")
def poophandler():
	return "<html><body><a href='poop'>Click here for poop!</a></body></html>"

@app.route("/getdrugs")
def drugsdealer():
	drugsrequest=requests.get("http://www.speciosa.com")
	return drugsrequest.text

@app.route("/totc")
def getbook():
	book=open("totc.txt")
	return book.read()

@app.route("/getshitname/<shitname>")
def shitnamehandler(shitname):
	if shitname=="josh":
		return "josh is the best name ever"
	return shitname+" is a shitty name "

@app.route("/dickhumiliator", methods=["GET", "POST"])
def dong():
	if request.method == 'POST':
		return request.form['penislength'] + " is so tiny, ha ha ha!"
	if request.method == 'GET':
		return render_template("index.html", hellostring="Welcome to the dick sizing thing")

    

if __name__ == "__main__":
    app.run(host="192.168.1.81")
