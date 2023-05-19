import requests
from json import JSONDecodeError
from main.exceptions import MadlibServiceUnavailable


class MadlibService:
    """
    Base Service for Madlib requests
    """
    def __init__(self):
        self.base_url = "https://reminiscent-steady-albertosaurus.glitch.me/"

    def get_random_words(self) -> (str, str, str):
        """
        Returns random words in a specific order based on Madlib response
        """
        return self._get_word("adjective"), self._get_word("verb"), self._get_word("noun")

    def _get_word(self, word_type: str) -> str:
        """
        Returns random word based on word_type
        :param word_type: type of the word to get (adjective, verb or noun)
        :return: generated word
        """
        full_url = self.base_url + "/" + word_type
        response = requests.get(full_url)
        response_json = self._compose_response(response)
        return response_json

    @staticmethod
    def _compose_response(response):
        """
        Handle errors
        """
        # Response compose in a case when we want to through an error if Madlib is unavailable
        try:
            response.raise_for_status()
            response_json = response.json()
        except (requests.HTTPError, JSONDecodeError):
            raise MadlibServiceUnavailable()
        return response_json
