""" Hello.py """
from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    """TODO: Docstring for show_blog.

    :p: TODO
    :returns: TODO

    """
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    """TODO: Docstring for revision.
    :returns: TODO

    """
    return 'Revision Number %f' % revNo

@app.route('/hello/<name>')
def hello_world(name):
    """TODO: Docstring for hello_world.
    :returns: TODO
    """
    return 'Hello %s!' % name

if __name__ == "__main__":
    app.run()
