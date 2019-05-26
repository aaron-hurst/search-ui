from flask import Flask, render_template#, flash, redirect, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('search.html')

if __name__=='__main__':
    app.run(debug=True)