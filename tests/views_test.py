class TestMain:

    def test_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код и """
        response = test_client.get('/', follow_redirects=True)
        assert response.status_code == 200, "Статус код постов неверный"

    def test_root_content(self, test_client):
        response = test_client.get('/', follow_redirects=True)
        assert "искать..." in response.data.decode("utf-8"), "Контент страницы неверный"

    def test_search_content(self, test_client):
        response = test_client.get('/search?s=1', follow_redirects=True)
        assert "Утром отправились на катере" in response.data.decode("utf-8"), "Контент страницы неверный"

    def test_if_post_exist_check(self, test_client):
        response = test_client.get('/posts/134313551', follow_redirects=True)
        assert "нет поста с номером" in response.data.decode("utf-8"), "Контент страницы неверный"

    def test_if_post_number(self, test_client):
        response = test_client.get('/posts/dsaffdsf', follow_redirects=True)
        assert "неверный тип" in response.data.decode("utf-8"), "Контент страницы неверный"
