from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hola gentuza!'

@app.route('/')
@app.route('/{name}')
def hola():
    name = {'nick': 'Angel'} #Añadimos un falso nick
    return render_template('hello.html',
                           name = name)

if __name__ == '__main__':
    app.debug = True
    app.run()
