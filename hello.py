from flask import Flask,render_template


#Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index(): new Change
#	return "<h1>Hello World!</h1>"

def index():
	firstName = "John"
	stuff = "This is bold text"

	favoritePizza=['Pepperoni','Cheese','Sausage',41]
	return render_template("index.html",
		firstName=firstName,
		stuff=stuff,
		favoritePizza=favoritePizza)

@app.route('/user/<name>')

def user(name):
	return render_template("user.html", userName=name)



# Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500
