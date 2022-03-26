import os
from flask import Flask, redirect, render_template, send_file, send_from_directory, url_for, request, flash
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename




app = Flask(__name__)
#This is my secret key
app.config['SECRET_KEY'] = b'X\x98\xb6\xaf5;\x00\xcb\xcf\xba\xbc\xb4\x98/\xc1`'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/WAD'
mongo = PyMongo(app)

#Redirect default route to the profile page route
@app.route("/", methods=['GET','POST'])
def SignIn():
    #Display Sign In page 
    if request.method == "GET":
        return render_template("form_auth.html")
    else:
         #store username and password from form
        username = request.form.get('username')
        password = request.form.get('password')

        #check username
        username_val = mongo.db.users.find_one({'username':username})
        password_val = mongo.db.users.find_one({'password':password})
        if  username_val and password_val:
            flash('Connected ')
            return redirect('/profile')
        #if a username doesn't existed
        else:
            flash('password or username incorrect ')
            return render_template("form_auth.html")

@app.route('/profile')
def secret_page():
    return render_template("profile.html")

#Define the icon of the site
@app.route("/favicon.ico")
def favicon():
    return send_from_directory("static","favicon.ico","assets/icon/icon2.png")
#Customize the error page
@app.errorhandler(404)
def page_not_found(error):
    return render_template('not_found_page.html'), 404
if __name__ == "__main__":
    app.run("localhost",port=5000,debug=True)