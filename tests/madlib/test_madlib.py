import mock
from django.urls import reverse


class TestMadlib:
    @classmethod
    def teardown_class(cls):
        pass

    @mock.patch(
        "main.services.MadlibService.get_random_words",
        return_value=("delightful", "hunt", "meatballs"),
    )
    def test_get_madlib_phrase(self, mock_get_random_words, api_client):
        url = reverse("madlib")
        response = api_client.get(url)
        mock_get_random_words.assert_called_once()
        assert response.json()["sentence"] == "It was a delightful day. I went downstairs to see if I could " \
                                              "hunt dinner. I asked, 'Does the stew need fresh meatballs?'"
        assert response.status_code == 200
