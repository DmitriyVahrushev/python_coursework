from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)