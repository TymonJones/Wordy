from flask import Flask, jsonify
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class LoginForm(FlaskForm):
    username = StringField('Username')
    submit = SubmitField('Login')

@app.route('/api/login', methods=['POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_id = form.username.data
        user = User(user_id)
        login_user(user)
        app.current_user = user  # Store user for demonstration purposes
        return jsonify({'success': True, 'user_id': user_id})
    return jsonify({'success': False, 'error': 'Invalid credentials'}), 401

@app.route('/api/logout')
@login_required
def logout():
    logout_user()
    app.current_user = None  # Clear stored user for demonstration purposes
    return jsonify({'success': True})

@app.route('/api/user')
@login_required
def get_user():
    return jsonify({'user_id': current_user.id})

if __name__ == '__main__':
    app.run(debug=True)


