import requests
from flask import Flask, render_template
from post import Post

DATA_LINK = "https://api.npoint.io/e9c7d09563544c2d60f6"
# POSTS_DATA = requests.get(DATA_LINK).json()
# ALL_POSTS = [Post(post["id"], post["title"], post["subtitle"], post["body"]) for post in POSTS_DATA]
ALL_POSTS = requests.get(DATA_LINK).json()
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


@app.route('/style-guide')
def style_guide():
    return render_template("style-guide.html")


@app.route('/contact')
def contact():
    return render_template("page-contact.html")


@app.route('/post')
def single_standard_post():
    return render_template('single-standard.html')


@app.route('/video-post')
def single_video_post():
    return render_template('single-video.html')


@app.route('/audio-post')
def single_audio_post():
    return render_template('single-audio.html')


if __name__ == "__main__":
    app.run(debug=True)
