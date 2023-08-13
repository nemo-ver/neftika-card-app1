from flask import Flask, render_template, request, send_file
import os
import tocken
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        startdate = request.form.get('startdate')
        finishdate = request.form.get('finishdate')
        # Call your Python program or function with input_data
        result = tocken.getdata(startdate,finishdate)
        return render_template('index.html', result=True, filepath=result)
    return render_template('index.html', result=None)

@app.route('/download/<filename>')
def download_file(filename):
    # Get the path to the file in the 'downloads' folder
    file_path = os.path.join('download', filename)
    
    # Use send_file to send the file for download
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)