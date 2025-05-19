import requests
from flask import Flask, render_template
from post import Post

DATA_LINK = "https://api.npoint.io/c790b4d5cab58020d391"
POSTS_DATA = requests.get(DATA_LINK).json()
ALL_POSTS = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in POSTS_DATA]

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index2.html", posts=ALL_POSTS)


@app.route('/post/<int:post_id>')
def post(post_id):
    for blog_post in ALL_POSTS:
        if blog_post.post_id == post_id:
            return render_template("post.html", post=blog_post)


@app.route('/about')
def about():
    return render_template("page-about.html")

@app.route('/category')
def category():
    return render_template("category.html")

if __name__ == "__main__":
    app.run(debug=True)
