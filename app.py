from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/contact')
def contact():
    return 'Contact form'

@app.route('/user/<username>', methods=['GET'])
def show_user_profile(username):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)