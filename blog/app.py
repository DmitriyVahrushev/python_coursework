from flask import Flask, render_template, url_for
from forms import RegistrationForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '43543fdgfdgt43'

posts = [
    {
          'author': 'Dmitriy',
          'title': 'This my first post',
          'date':"2014",
          'content': 'This is blog about me.'  
    },
    {
          'author': 'Dmitriy',
          'title': 'About my hobbies',
          'date':"2014",
          'content': 'My hobbies are Python and so on.'  
    }
]

@app.route('/')
def homepage():
    return render_template('main.html', posts = posts)


@app.route('/about')
def about():
    return render_template('about.html', title = "About my blog")

@app.route('/register', methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title = "Register", form = form)

if __name__ == '__main__':
    app.run(debug=True)