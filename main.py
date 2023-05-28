from flask import Flask
from posts.views import posts_blueprint
from comments.views import comments_blueprint
from bookmarks.views import bookmarks_blueprint
from api.views import api_blueprint
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(posts_blueprint)
app.register_blueprint(comments_blueprint)
app.register_blueprint(api_blueprint)
app.register_blueprint(bookmarks_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return f"<p>Страница не найдена<br><br>{e}</p>",\
           f"<p><a href='/'>обратно</a></p>", 404


@app.errorhandler(500)
def page_server_error(e):
    return f"<p>Ошибка на сервере:<br><br>{e}</p>"\
           f"<p><a href='/'>обратно</a></p>", 500


if __name__ == "__main__":
    app.run(port=8000)
