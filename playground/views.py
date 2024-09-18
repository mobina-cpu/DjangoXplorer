from django.shortcuts import render
from rest_framework.views import APIView
import logging
import requests

logger = logging.getLogger(__name__)


class HelloView(APIView):
    @staticmethod
    def get(request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response ')
            data = response.json()
        except ConnectionError:
            logger.critical('httpbin is offline')

        return render(request, 'hello.html', {'name': 'Mobina'})
