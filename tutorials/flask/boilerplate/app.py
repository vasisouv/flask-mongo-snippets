from flask import Flask, render_template

app = Flask(__name__, template_folder='views')


@app.route("/")
def home():
    uni_name = "Aristotle University of Thessaloniki"
    return render_template('some_html_file.html', uni_name=uni_name)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5110)
