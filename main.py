
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.urls import url_parse
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///airbnb_spain.db'
db = SQLAlchemy(app)

# Define the database model for properties
class Property(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)

# Define the main route
@app.route('/')
def home():
    # Retrieve all properties from the database
    properties = Property.query.all()
    # Render the home page template with the properties
    return render_template('home.html', properties=properties)

# Define the search route
@app.route('/search', methods=['POST'])
def search():
    # Retrieve the search query from the request
    query = request.form['query']
    # Search the database for properties that match the query
    properties = Property.query.filter(Property.title.like('%' + query + '%'))
    # Redirect to the search results page with the properties
    return render_template('search_results.html', properties=properties)

# Define the property detail route
@app.route('/property_detail/<int:id>')
def property_detail(id):
    # Retrieve the property with the specified ID from the database
    property = Property.query.get(id)
    # Render the property detail page template with the property
    return render_template('property_detail.html', property=property)

# Define the book route
@app.route('/book/<int:property_id>', methods=['POST'])
def book(property_id):
    # Retrieve the property with the specified ID from the database
    property = Property.query.get(property_id)
    # Redirect to the user dashboard page
    return redirect(url_for('user_dashboard'))

# Define the user dashboard route
@app.route('/user_dashboard')
def user_dashboard():
    # Render the user dashboard template
    return render_template('user_dashboard.html')

# Define the host dashboard route
@app.route('/host_dashboard')
def host_dashboard():
    # Render the host dashboard template
    return render_template('host_dashboard.html')

# Define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Get the next URL from the request
    next_url = request.args.get('next') or request.form.get('next')
    if request.method == 'GET':
        # Render the login page template
        return render_template('login.html')
    else:
        # Get the username and password from the request
        username = request.form['username']
        password = request.form['password']
        # Authenticate the user
        if username == 'admin' and password == 'password':
            # Redirect to the next URL or the home page if the next URL is not specified
            return redirect(next_url or url_for('home'))
        else:
            # Render the login page template with an error message
            return render_template('login.html', error="Invalid username or password")

# Define the logout route
@app.route('/logout')
def logout():
    # Redirect to the home page
    return redirect(url_for('home'))

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
