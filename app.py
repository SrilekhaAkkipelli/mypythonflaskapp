import flask
from flask import Flask, request, render_template
from flask import app
@app.route('/')
def index():
    return render_template('register.html')
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return render_template('success.html', name=name, email=email)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
   