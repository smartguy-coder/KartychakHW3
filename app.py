# pip install -r requirements.txt
from flask import Flask, render_template, url_for, request, flash
import database_module
import os

# main functions for web develop========================================================================================


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


menu = [{'name': "All posts", "url": "index"},
        {'name': "Add post", 'url': 'new_post'},
        {'name': "Edit post", 'url': 'edit_post'},
        {'name': "Delete post", 'url': 'delete_post'},]


# 404 error leads us to the main page
@app.errorhandler(404)
def handle_bad_request(e):
    all_posts = database_module.select_all_posts()
    return render_template("index.html", title="All posts", all_posts=all_posts, menu=menu)

@app.route("/index")
@app.route("/")
def main_page_all_posts():
    """main page with all posts"""

    all_posts = database_module.select_all_posts()

    return render_template("index.html", title="All posts", all_posts=all_posts, menu=menu)


@app.route("/new_post", methods=['POST', 'GET'])
def new_post_page():
    """here you can add a new post"""

    if request.method == "POST":
        title = request.form['new_post_title']
        description = request.form['new_post_description']
        database_module.add_new_post(title, description)

        flash(f"New post was added: title -> {title}, description -> {description}", category='add_post')

    return render_template("new_post.html", menu=menu)


@app.route("/edit_post", methods=['POST', 'GET'])
def edit_post_page():
    """here you can edit post than exists"""

    if request.method == "POST":
        try:
            identifier = int(request.form["id_post_for_edit"])
        except ValueError:
            flash(f"You have entered not integer value for ID", category='deleted')
            return render_template("edit_post.html",  menu=menu)

        if identifier not in database_module.list_of_id():
            flash(f"There is no post with id={identifier}", category='deleted')
            return render_template("edit_post.html", menu=menu)

        title = request.form['edit_post_title']
        description = request.form['edit_post_description']
        database_module.edit_post(identificator, title, description)

        flash(f"Yoy have edited post", category='add_post')

    return render_template("edit_post.html",  menu=menu)


@app.route("/delete_post", methods=['POST', 'GET'])
def delete_post_page():
    """here you can delete post than exists"""

    if request.method == "POST":
        try:
            identifier = int(request.form["id_post_for_delete"])
        except ValueError:
            flash(f"You have entered not integer value for ID", category='deleted')
            return render_template("delete_post.html",  menu=menu)

        if identifier not in database_module.list_of_id():
            flash(f"There is no post with id={identifier}", category='deleted')
            return render_template("delete_post.html", menu=menu)

        database_module.delete_post(identifier)

        flash(f"Yoy have deleted post", category='deleted')

    return render_template("delete_post.html",  menu=menu)


if __name__ == '__main__':
    database_module.create_database()
    app.run(debug=True)