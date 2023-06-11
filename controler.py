from pyramid.response import Response

class HomeController:
    def index(self, request):
        return Response('Hello, World!')

    def about(self, request):
        return Response('a propos de la page')