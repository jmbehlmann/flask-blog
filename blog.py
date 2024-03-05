from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '1'

posts = [
    {
        'author': 'James',
        'title': 'Post 1',
        'content': 'this is the first post',
        'date_posted': 'February 19, 2024'
    },
    {
        'author': 'James',
        'title': 'Post 2',
        'content': 'this is the second post',
        'date_posted': 'February 19, 2024'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Accout created for {form.email.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'{form.email.data} is now logged in!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
