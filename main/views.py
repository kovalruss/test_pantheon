from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import MadlibRetrieveResponseSerializer
from main.services import MadlibService
from main.exceptions import MadlibServiceUnavailable


@extend_schema(tags=["Madlib"])
class MadlibAPIView(APIView):
    @extend_schema(
        responses={
            200: MadlibRetrieveResponseSerializer,
            503: MadlibServiceUnavailable,
        },
    )
    def get(self, request):
        """
        Get a constant phrase formatted with random words from Madlib
        """
        madlib_service = MadlibService()
        adjective, verb, noun = madlib_service.get_random_words()
        formatted_sentence = f'It was a {adjective} day. I went downstairs to see if I could {verb} dinner. ' \
                             f'I asked, \'Does the stew need fresh {noun}?\''

        serialized_response = MadlibRetrieveResponseSerializer(data={"sentence": formatted_sentence})
        serialized_response.is_valid(raise_exception=True)

        return Response(data=serialized_response.data, status=status.HTTP_200_OK)
