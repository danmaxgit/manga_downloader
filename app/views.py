# Flask modules
from flask               import render_template, request, url_for, redirect, jsonify
from flask_login         import login_user, login_required

# App modules
from app        import app, lm, bcrypt
from app.models import User
from app.forms  import LoginForm

import requests

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = request.form.get('username', '', type=str)
        password = request.form.get('password', '', type=str)
        
        user = User.query.filter_by(user=username).first()
        if user:
            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('index'))
    return render_template('singin.html', form=form)

@login_required
@app.route('/index')
def index():
    return render_template('grid.html')

@login_required
@app.route('/api', methods=['GET'])
def search():
    user_agents = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
    st_accept = "text/html"
    headers = {
        "Accept": st_accept,
        "User-Agent": user_agents
    }

    resp = requests.get('https://mangalib.me/', headers)#add here selenium
    if resp.status_code == 200:
        return jsonify({"a":"b"})