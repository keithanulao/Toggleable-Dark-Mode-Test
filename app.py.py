#Dark Mode Website Test

from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

dark_mode = False

@app.route('/')
def index():
    global dark_mode  # Access global variable
    return render_template('index.html', dark_mode=dark_mode)

@app.route('/toggle_theme')
def toggle_theme():
    global dark_mode  # Access and modify global variable
    dark_mode = not dark_mode  # Toggle state
    return render_template('index.html', dark_mode=dark_mode)

if __name__ == '__main__':
    app.run(debug=True)