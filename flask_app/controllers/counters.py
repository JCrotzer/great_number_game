from flask_app import app
import random
from flask import render_template, redirect, request, session, flash


@app.route('/')
def index():
    if 'num' not in session:
        session['num'] = random.randint(1,100)
    return render_template('index.html')
    
@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
