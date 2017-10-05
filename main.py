from flask import Flask, request, render_template
import cgi 

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup", methods=['POST'])
def errors():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email_address = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) < 3 or len(username) > 20:
        username_error = 'That is not a valid username'
    elif len(password) < 3 or len(password) > 20:
        password_error = 'That is not a valid password'
    elif verify != password:
        verify_error = 'passwords do not match'
    elif email_address != "" and len(email_address) < 3 or len(email_address) > 20:
        email_error = 'That is not a valid email'
    elif email_address != "" and ("." not in email_address or "@" not in email_address):
        email_error = 'Not a valid email.'

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template('welcome.html', username=username)
    else:
        return render_template('confirmation.html', username_error=username_error, password_error=password_error, 
        verify_error=verify_error, email_error=email_error )
    


@app.route("/")
def index():
    return render_template('confirmation.html')



app.run()