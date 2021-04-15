import cfscrape
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from bs4 import BeautifulSoup

from usuario.services import validate_token_user
from .models import Game
from .serializers import GameSerializer
from datetime import datetime, timedelta


class GameView(APIView):
    def get(self, request):
        valid = validate_token_user(request.headers)

        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])
        user_object = valid['user']

        games = GameSerializer(Game.objects.filter(
            user=user_object), many=True).data

        return Response(games)

    def post(self, request):
        if request.data['tens'] < 6 or request.data['tens'] > 10:
            return Response('numero de dezenas invalido', 400)

        valid = validate_token_user(request.headers)
        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])

        numbers = str(sorted([random.randint(1, 60)
                              for i in range(request.data['tens'])]))
        user_object = valid['user']
        game_object = Game.objects.create(numbers=numbers, user=user_object)
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
        data = data.decode('utf-8')
        soup = BeautifulSoup(data, "html.parser")

        concurse = soup.find("span", class_="qLLird").span.text
        concurse_result = [int(span.text) for span in list(
            soup.find("div", class_="MDTDab").children)]

        return Response({"concurso": concurse, "numeros": concurse_result})


class PointsView(APIView):
    def get(self, request):
        valid = validate_token_user(request.headers)

        if valid['response'] != True:
            return Response({'response': valid['response']}, valid['status'])

        user_object = valid['user']

        url = "https://www.google.com/search?q=resultado+mega+sena"
        scraper = cfscrape.create_scraper()
        data = scraper.get(url).text
        soup = BeautifulSoup(data, "html.parser")
        concurse = soup.find("span", class_="qLLird").span.text
        concurse_date = datetime.strptime(
            concurse.split()[2].strip('(').strip(')'), '%d/%m/%y')

        game = GameSerializer(Game.objects.filter(
            user=user_object), many=True).data[-1]
        game_date = datetime.strptime(game['date'],'%Y-%m-%d')
        
        if game_date < concurse_date:
            return Response('resultado ainda está indisponivel')

        concurse_result = [int(span.text) for span in list(
            soup.find("div", class_="MDTDab").children)]

        game_numbers = [int(number) for number in game['numbers'].strip(
            '[').strip(']').split(',')]

        points = 0

        for number in game_numbers:
            if number in concurse_result:
                points += 1

        return Response({'points': points, "game": game,"concurse": concurse, "result_numbers": concurse_result, "game_numbers": game_numbers})
