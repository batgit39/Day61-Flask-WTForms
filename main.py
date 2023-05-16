from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email() ]) 
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')
#NOTE: the label field is added here to understand what the field is used for it's not necessary for the code 


app = Flask(__name__)
app.config['SECRET_KEY'] = 'asdfghjkl'
Bootstrap(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login.html", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.email.data
        password = form.password.data
        if username == 'admin69@gmail.com' and password == '1234567':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
