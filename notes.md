# Dev Notes

## Flask Basics
- `@app.route('/path')` maps a URL to a Python function
- `render_template('file.html')` serves an HTML file from the templates folder
- `request.form` accesses POST data from HTML forms

## Templates
- `base.html` holds the shared layout — all other templates extend it
- `{% block content %}` is the slot that child templates fill in
- `url_for('function_name')` generates URLs dynamically — better than hardcoding
