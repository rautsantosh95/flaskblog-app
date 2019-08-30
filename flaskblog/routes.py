from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author' : 'santosh1',
        'title' : 'Blog post 1',
        'content' : 'first post content',
        'date_posted' : 'Agust 21, 2019'
    },
    {
        'author' : 'santosh2',
        'title' : 'Blog post 2',
        'content' : 'second post content',
        'date_posted' : 'Agust 22, 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash=(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title=register, form=form)

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You Have Been Logged In!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Unsuccessful Login. Please Check Username and Password', 'danger')
    return render_template('login.html', title=login, form=form)
