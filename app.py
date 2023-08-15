from flask import Flask, render_template, request, send_file, redirect, url_for, session
from pymongo import MongoClient
import bcrypt
import os
import tocken
app = Flask(__name__)


# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client['auth_demo']
users = db['users']

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password'].encode("utf-8")
        
        user = users.find_one({'username': username})
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session["username"] = username
            # Successful login
            return redirect(url_for('index'))
        else:
            # Failed login
            return "Invalid login credentials"
    
    return render_template('login.html')













@app.route('/', methods=['GET', 'POST'])
def index():
    if "username" in session:
        if request.method == 'POST':
            startdate = request.form.get('startdate')
            finishdate = request.form.get('finishdate')
            # Call your Python program or function with input_data
            result = tocken.getdata(startdate,finishdate)
            return render_template('index.html', result=True, filepath=result)
        return render_template('index.html', result=None)
    else:
        return redirect("/login")

@app.route('/download/<filename>')
def download_file(filename):
    # Get the path to the file in the 'downloads' folder
    file_path = os.path.join('download', filename)
    
    # Use send_file to send the file for download
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)