import json


class BookmarksDAO:

    def __init__(self, path):
        self.path = path

    def _load(self):
        with open(self.path, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data

    def _write(self, data):
        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def get_bookmarks_all(self):
        """возвращает закладки"""
        bookmarks = self._load()
        return bookmarks

    def del_bookmark(self, selected_bokmark):
        """удаляет закладку"""
        bookmarks = self._load()
        for bookmark in bookmarks:
            if bookmark == selected_bokmark:
                bookmarks.remove(bookmark)
        self._write(bookmarks)

    def add_bookmark(self, bookmark):
        """добавляет закладку"""
        bookmarks = self._load()
        if int(bookmark) not in bookmarks:
            bookmarks.append(int(bookmark))
        self._write(bookmarks)
