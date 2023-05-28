from flask import Blueprint, jsonify
from posts.dao.posts_dao import PostsDAO
import api.logger as log


api_blueprint = Blueprint('api_blueprint', __name__)
# Создаем DAO
posts_dao = PostsDAO("data/data.json")


@api_blueprint.route('/api/posts')
def page_api_posts():
    log.api_logger.info('Запрос /api/posts')
    posts = posts_dao.get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<postid>')
def page_api_postid(postid):
    log.api_logger.info(f'Запрос /api/posts/{postid}')
    try:
        post = posts_dao.get_post_by_pk(int(postid))
    except ValueError:
        return f'неверный тип данных: {postid}'
    if not post:
        return f'нет поста с номером: {postid}'
    return jsonify(post)
