from flask import Flask, render_template, redirect, jsonify  
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    user = User()
    user.id = user_id
    return user

class LoginForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Login')

@app.route('/api/login', methods=['POST'])  # Updated route to /api/login
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User()
        user.id = form.username.data
        login_user(user)
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Invalid credentials'}), 401

@app.route('/api/logout')  # Updated route to /api/logout
@login_required
def logout():
    logout_user()
    return jsonify({'success': True})

@app.route('/api/user')  # Updated route to /api/user
@login_required
def get_user():
    return jsonify({'username': current_user.id})

if __name__ == '__main__':
    app.run(debug=True)


