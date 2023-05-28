from flask import Blueprint, render_template, redirect
from bookmarks.dao.bookmarks_dao import BookmarksDAO
from posts.dao.posts_dao import PostsDAO

bookmarks_blueprint = Blueprint('bookmarks_blueprint', __name__, template_folder='templates')
# Создаем DAO
bookmarks_dao = BookmarksDAO("data/bookmarks.json")
posts_dao = PostsDAO("data/data.json")


@bookmarks_blueprint.route('/bookmarks/add/<postid>')
def page_add_bookmark(postid):
    bookmarks_dao.add_bookmark(postid)
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks/remove/<postid>')
def page_del_bookmark(postid):
    bookmarks_dao.del_bookmark(int(postid))
    return redirect("/", code=302)


@bookmarks_blueprint.route('/bookmarks')
def page_bookmarks():
    bookmarks = bookmarks_dao.get_bookmarks_all()
    posts = []
    for bookmark in bookmarks:
        posts.append(posts_dao.get_post_by_pk(bookmark))
    return render_template("bookmarks.html", posts=posts)
