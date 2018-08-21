from flask import Flask, render_template
from tutorials.demo_yelp_app.backend import db

app = Flask(__name__, template_folder='views')


@app.route("/")
def home():
    num_of_restaurants = db.find_count('restaurants')
    num_of_users = db.find_count('users')
    num_of_reviews = db.find_count('reviews')

    return render_template('home.html', num_of_restaurants=num_of_restaurants, num_of_users=num_of_users,
                           num_of_reviews=num_of_reviews)


@app.route("/restaurants")
def restaurants():
    top_10_restaurants = db.find_top_restaurants(10)
    top_10_restaurants = list(top_10_restaurants)

    return render_template('restaurants.html', top_10_restaurants=top_10_restaurants)


@app.route("/users")
def customers():
    random_reviews = db.find_random_reviews(5)
    return render_template('users.html', random_reviews=random_reviews)


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5110)
