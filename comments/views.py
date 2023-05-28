from flask import Blueprint

comments_blueprint = Blueprint('comments_blueprint', __name__)


@comments_blueprint.route('/comments/')
def page_index():
    return "Comments work"
