from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index ():
    user = {'username' : 'Ronnie'}
    posts = [

        {
            'author': {'username': 'Jack'},
            'body': 'I am the anal sax batman'
        },
        {
            'author': {'username' : 'John'},
            'body': 'Beautiful day in portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool'

        }



    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
    app.run()
