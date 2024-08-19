from flask import render_template

from flask import Flask

app = Flask(__name__)


def error(errorCode, errorMsg):
    return render_template('/errorpage.html', code=errorCode, message=errorMsg)


@app.route('/')
@app.route('/<name>')
def hello(name="Anonymus"):
    return render_template('/demopage.html', user=name)


@app.route('/user/<username>')
def user_page(username=None):

    if True:
        return render_template('/user.html', user=username)
    else:
        return error(404, "User not found!")
    
@app.route('/search/<search>')
def search(search=None):

    if search != None:
        return error(200, "Searched: "+search)
    else:
        return error(404, "Searched item not found!")


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)