from flask import Flask
from flask import render_template
app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello_world():
    return 'Hola gentuza!'

@app.route('/')
@app.route('/{name}')
def hola():
    name = {'nick': 'Angel'}
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('hello.html',
                           name = name,
                           posts = posts)

if __name__ == '__main__':
    app.debug = True
    app.run()
