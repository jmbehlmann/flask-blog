from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = ''

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

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login  ")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
