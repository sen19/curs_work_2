import json


class CommentsDAO:

    def __init__(self, path):
        self.path = path

    def _load(self):
        with open(self.path, "r", encoding="utf-8") as file:
            comments = json.load(file)
        return comments

    def get_all(self):
        comments = self._load()
        return comments

    def get_comments_by_post_id(self, post_id):
        """возвращает комментарии определенного поста. Функция должна вызывать ошибку `ValueError` если такого поста нет и пустой список, если у поста нет комментов."""
        comments = self._load()
        findings = []
        for comment in comments:
            if comment['post_id'] == post_id:
                findings.append(comment)
        return findings
