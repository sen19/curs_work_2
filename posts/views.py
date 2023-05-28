from flask import Blueprint, render_template, request
from posts.dao.posts_dao import PostsDAO
from comments.dao.comments_dao import CommentsDAO
from bookmarks.dao.bookmarks_dao import BookmarksDAO


posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates')
# Создаем DAO
posts_dao = PostsDAO("data/data.json")
comments_dao = CommentsDAO("data/comments.json")
bookmarks_dao = BookmarksDAO("data/bookmarks.json")


@posts_blueprint.route('/')
def page_index():
    posts = posts_dao.get_all_posts_with_tags()
    bookmarks_count = len(bookmarks_dao.get_bookmarks_all())
    return render_template("index.html", posts=posts, bk_count=bookmarks_count)


@posts_blueprint.route('/posts/<postid>')
def page_postid(postid):
    try:
        post = posts_dao.get_post_by_pk(int(postid))
    except ValueError:
        return f'неверный тип данных: {postid}'
    if not post:
        return f'нет поста с номером: {postid}'
    comments = comments_dao.get_comments_by_post_id(int(postid))
    return render_template("post.html", post=post, comments=comments)


@posts_blueprint.route('/search/', methods=['GET'])
def page_search():
    s = request.args.get("s", "")
    posts = posts_dao.search_for_posts(s)
    return render_template("search.html", posts=posts)


@posts_blueprint.route('/users/<poster_name>')
def page_user_feed(poster_name):
    posts = posts_dao.get_posts_by_user(poster_name)
    return render_template("user-feed.html", posts=posts)


@posts_blueprint.route('/tag/<tag_name>')
def page_tag(tag_name):
    posts = posts_dao.search_for_posts(tag_name)
    return render_template("tag.html", posts=posts)
