# Dev Notes

## Flask Basics
- `@app.route('/path')` maps a URL to a Python function
- `render_template('file.html')` serves an HTML file from the templates folder
- `request.form` accesses POST data from HTML forms

## Templates
- `base.html` holds the shared layout — all other templates extend it
- `{% block content %}` is the slot that child templates fill in
- `url_for('function_name')` generates URLs dynamically — better than hardcoding

## Routes in this project
- `GET /` — home, list all users/countries
- `POST /form` — accepts new entry from form
- `GET/POST /update_country/<name>` — edit an existing entry
- `GET /404` — custom 404 error page

## Notebook
- `intro flask notes.ipynb` contains step-by-step Flask experiments
- Useful for testing snippets before adding to main.py

## Static Files
- CSS lives in `static/style.css`
- Referenced in templates with `url_for('static', filename='style.css')`
- Flask serves static files automatically from the `static/` folder
