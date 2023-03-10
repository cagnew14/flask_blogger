from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#Create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"
# Create a Form Class
class NamerForm(FlaskForm):
	name = StringField('What is your Name?', validators=[DataRequired()])
	submit = SubmitField('Submit')


# Create a route decorator
@app.route('/')

#def index(): 
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


# Create Name Page
@app.route('/name', methods=['GET','POST'])
def name():
	name = None
	form = NamerForm()
	# Validate Form
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
	return render_template("name.html",
		name = name,
		form = form)





