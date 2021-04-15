import cfscrape
import random

from rest_framework.views import APIView
from rest_framework.response import Response
from bs4 import BeautifulSoup
from lxml import etree

from usuario.services import validate_token_user
from .models import Game
from .serializers import GameSerializer


class GameView(APIView):
    def get(self, request):
        valid = validate_token_user(request.headers)

        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])
        user_object = valid['user']
        
        games = GameSerializer(Game.objects.filter(user=user_object),many=True).data
        
        return Response(games)

    def post(self, request):
        valid = validate_token_user(request.headers)

        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])
        
        numbers = str(sorted([random.randint(1, 60)
                         for i in range(request.data['tens'])]))
        user_object = valid['user']
        game_object = Game.objects.create(numbers=numbers,user=user_object)
        game = GameSerializer(game_object).data

        return Response(game)

class ResultView(APIView):
    def get(self, request):
        valid = validate_token_user(request.headers)

        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])

        url = "https://www.google.com/search?q=resultado+mega+sena"
        scraper = cfscrape.create_scraper()
        data = scraper.get(url).content
        soup = BeautifulSoup(data, "html.parser")

        concurse = soup.find("span", class_="qLLird").span.text
        concurse_result = [int(span.text) for span in list(
            soup.find("div", class_="MDTDab").children)]

        return Response({"concurso": concurse, "numeros": concurse_result})