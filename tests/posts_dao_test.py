from posts.dao.posts_dao import PostsDAO
import pytest

# Нам пригодится экземпляр DAO, так что мы создадим его в фикстуре
# Но пригодится только один раз, поэтому выносить в conftest не будем


@pytest.fixture()
def posts_dao():
    posts_dao_instance = PostsDAO("./data/data.json")
    return posts_dao_instance

# Задаем, какие ключи ожидаем получать у поста


keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}


class TestPostsDao:

    def test_get_all(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается """
        posts = posts_dao.get_posts_all()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_id(self, posts_dao):
        """ Проверяем, верный ли пост возвращается при запросе одного """
        post = posts_dao.get_post_by_pk(1)
        assert(post["pk"] == 1), "возвращается неправильный пост"
        assert set(post.keys()) == keys_should_be, "неверный список ключей"

    def test_get_by_user(self, posts_dao):
        """ Проверяем, верно ли отрабатывает выбор по юзеру"""
        with pytest.raises(ValueError, match=r"нет.*"):
            posts_dao.get_posts_by_user('skjljkjds')

    def test_search_for_post(self, posts_dao):
        """ Проверяем, верно ли отрабатывает поиск"""
        posts = posts_dao.search_for_posts('а')
        assert type(posts) == list, "возвращается не список"
        assert(len(posts) > 1), "ничего не найдено и это странно"

    def test_get_all_with_tags(self, posts_dao):
        """ Проверяем, верный ли список постов возвращается """
        posts = posts_dao.get_all_posts_with_tags()
        assert type(posts) == list, "возвращается не список"
        assert len(posts) > 0, "возвращается пустой список"
        assert set(posts[0].keys()) == keys_should_be, "неверный список ключей"
