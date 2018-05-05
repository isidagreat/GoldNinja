from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key="spaceship"


@app.route("/")
def index():
	if "gold" not in session:
		session["gold"]= 0

	session["comments"] = ""
	return render_template("index.html")

@app.route("/process_money", methods=["POST"])
def lotto():
	
	if request.form["building"] == "Garage":
		x = random.randrange(10,20)
		session["gold"] += x
		return redirect("/")
	elif request.form["building"] == "kitchen":
		x = random.randrange(5,10)
		session["gold"] += x
		return redirect("/")
	elif request.form["building"] == "cemetary":
		x = random.randrange(2,5)
		session["gold"] += x
		return redirect("/")
	else:
		x = random.randrange(0,50)
		if x % 2 == 1:
			session["gold"] -= x
		else:
			session["gold"] += x 



		return redirect("/")

	

if __name__ == "__main__":
	app.run(debug=True)