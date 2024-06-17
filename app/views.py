
# Flask modules
from flask               import render_template, request, url_for, redirect, send_from_directory, flash
from flask_login         import login_user, logout_user, current_user, login_required
from werkzeug.exceptions import HTTPException, NotFound, abort
from jinja2              import TemplateNotFound
from werkzeug.security   import generate_password_hash, check_password_hash

# App modules
from app        import app, db
from app.models import User
from app.forms  import LoginForm, RegisterForm

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # апроверкп вхрда

        return redirect(url_for('index'))
    return render_template('singin.html', form=form)

@app.route('/index')
def index():
    return render_template('grid.html')