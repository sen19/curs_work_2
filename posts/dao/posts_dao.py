import json


class PostsDAO:

    def __init__(self, path):
        self.path = path

    def _load(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def get_posts_all(self):
        """возвращает посты"""
        posts = self._load()
        return posts

    def get_posts_by_user(self, user_name):
        """возвращает посты определенного пользователя. Функция должна вызывать ошибку `ValueError` если такого пользователя нет и пустой список, если у пользователя нет постов."""
        posts = self.get_all_posts_with_tags()
        findings = []
        for post in posts:
            if post['poster_name'].lower() == user_name.lower():
                findings.append(post)
        if len(findings) == 0:
            raise ValueError(f'нет такого пользователя: {user_name}')
        else:
            return findings

    def search_for_posts(self, query):
        """возвращает список постов по ключевому слову"""
        posts = self.get_all_posts_with_tags()
        findings = []
        for post in posts:
            if query.lower() in post['content'].lower():
                findings.append(post)
                if len(findings) >= 10:
                    break
        return findings

    def get_post_by_pk(self, pk):
        """возвращает один пост по его идентификатору"""
        posts = self.get_all_posts_with_tags()
        try:
            for post in posts:
                if post['pk'] == pk:
                    return post
            return False
        except TypeError:
            raise f'неверный тип данных: {pk}'

    def get_all_posts_with_tags(self):
        """превращает теги в ссылки"""
        posts = self._load()
        try:
            for post_num in range(len(posts)):
                words_in_post = posts[post_num]['content'].split(' ')
                for word_num in range(0, len(words_in_post)):
                    if words_in_post[word_num][0] == '#':
                        words_in_post[word_num] = f"<a href='/tag/%23{words_in_post[word_num][1:]}' class='item__tag'>{words_in_post[word_num]}</a>"
                posts[post_num]['content'] = ' '.join(words_in_post)
        except TypeError:
            raise f'неверный тип данных'
        finally:
            return posts
