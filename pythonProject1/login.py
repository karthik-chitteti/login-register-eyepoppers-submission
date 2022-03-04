from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__)


def check_login(username, password):
    if username == 'Thor' and password == 'pointbreak':
        return True
    else:
        return False


@app.route('/<user>', methods=['POST', 'GET'])
def user_name(user):
    message = f'welcome {user}'
    return render_template('home.html', message=message)


@app.route('/login', methods=['POST', 'GET'])
def login():
    message = None
    if request.method == 'POST':
        if check_login(request.form['username'], request.form['password']):
            message = f'Login Success, Welcome {request.form["username"]}'
            return redirect(url_for('user_name', user=request.form["username"]))
        else:
            message = 'Invalid credentials, Try again...'
    return render_template('login.html', message=message)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return f'Registering {request.form["usr"]}...'
    else:
        return render_template('register.html')


@app.route('/')
def main():
    return "This is main page of the website"


if __name__ == '__main__':
    app.run()
