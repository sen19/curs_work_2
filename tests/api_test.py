class TestApi:

    def test_root_status(self, test_client):
        """ Проверяем, получается ли нужный статус-код и """
        response = test_client.get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код api неверный"
        response = test_client.get('/api/posts/1', follow_redirects=True)
        assert response.status_code == 200, "Статус код api неверный"

    def test_if_post_exist_check(self, test_client):
        response = test_client.get('/api/posts/134313551', follow_redirects=True)
        assert "нет поста с номером" in response.data.decode("utf-8"), "Контент страницы неверный"
