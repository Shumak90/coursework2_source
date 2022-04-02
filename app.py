from flask import Flask, request, render_template, jsonify
from utils import DataComments

app = Flask(__name__)

data = DataComments("./data/data.json", "./data/comments.json")


@app.route("/")
def index():
    return render_template("index.html", all_post=data.get_posts_all())


@app.route("/posts/<int:postid>")
def post(postid):
    post_id = data.get_post_by_pk(postid)
    comments_id = data.get_comments_by_post_id(postid)
    comments_all = len(comments_id)
    return render_template("post.html", post_id=post_id, comments_id=comments_id, comments_all=comments_all)


@app.route("/search/")
def search():
    s = request.args.get("s")
    data_search = data.search_for_posts(s)
    len_data = len(data_search)
    return render_template("search.html", data_s=data_search, s=s, len_data=len_data)


@app.route("/users/<username>")
def users(username):
    users = data.get_posts_by_user(username)
    return render_template("user-feed.html", users=users)


@app.route("/api/posts")
def get_json_post():
    data_post = data.get_posts_all()
    return jsonify(data_post)


@app.route("/api/posts/<int:post_id>")
def get_json_post_id(post_id):
    post_id = data.get_post_by_pk(post_id)
    return jsonify(post_id)


@app.route("/bookmarks/")
def get_bookmarks():
    return render_template("bookmarks.html")


if __name__ == '__main__':
    app.run(debug=True)
