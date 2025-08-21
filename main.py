from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample user data
users = {
    'Alice': {'age': 25, 'country': 'USA'},
    'Bob': {'age': 30, 'country': 'UK'},
    'Charlie': {'age': 35, 'country': 'Australia'}
}

# Route: Home Page
@app.route('/')
def home():
    # "name" from GET params, default to "shen"
    name = request.args.get("name", "shen")

    # Current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # variables into template (now includes users)
    return render_template(
        "home.html",
        name=name,
        current_time=current_time,
        users=users
    )


# Route: Show All Users
@app.route('/all-users')
def all_users():
    return render_template("all_users.html", users=users)


# Route: Simple Form
@app.route('/form')
def form():
    return render_template("form.html")


@app.route('/update-country', methods=['GET', 'POST'])
def update_country():
    message = None

    if request.method == 'POST':

        username = request.form['username']
        new_country = request.form['country']

        # Update user if exists
        if username in users:
            users[username]['country'] = new_country
            message = f"{username}'s country has been updated to {new_country}!"
        else:
            message = f"User {username} not found."

    # Render template with current users and message
    return render_template("update_country.html", users=users, message=message)



@app.route('/greet/<name>')
def greet(name):
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template(
        "home.html",
        name=name,
        current_time=current_time,
        users=users  # pass the updated users dictionary
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5007, debug=True)

