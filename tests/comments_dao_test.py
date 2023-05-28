from comments.dao.comments_dao import CommentsDAO
import pytest

# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
# Но пригодится только один раз, поэтому выносить в conftest не будем


@pytest.fixture()
def comments_dao():
    comments_dao_instance = CommentsDAO("./data/comments.json")
    return comments_dao_instance

# Задаем, какие ключи ожидаем получать у поста


keys_should_be = {"post_id", "commenter_name", "comment", "pk"}


class TestCommentsDao:

    def test_comments_by_postid(self, comments_dao):
        """ Проверяем, верный ли пост возвращается при запросе одного """
        comments = comments_dao.get_comments_by_post_id(1)
        assert(comments[0]['post_id'] == 1), "возвращается неправильный пост"
        assert set(comments[0].keys()) == keys_should_be, "неверный список ключей"
        assert type(comments) == list, "возвращается не список"
