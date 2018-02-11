""" Hello.py """
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_world(name):
    """TODO: Docstring for hello_world.
    :returns: TODO
    """
    return 'Hello %s!' % name

if __name__ == "__main__":
    app.run()
