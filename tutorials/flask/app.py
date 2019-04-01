from flask import Flask, render_template
from tutorials.flask.demo_todo_app.db import Db

app = Flask(__name__, template_folder='views')
db = Db()


@app.route("/", methods=['GET'])
def home():
    todos = db.find_all('todos')
    return render_template('home.html', todos=list(todos))


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5110)
