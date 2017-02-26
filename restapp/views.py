from django.contrib.auth.models import User
from django.http import Http404
from counter import run
import json

from rest_framework.views import APIView
from rest_framework.response import Response


class StatsForAllSite(APIView):
    def get(self, request, format=None):
        return Response(run())

class StatsForAuthor(APIView):
    def get(self, request, format=None):
        return Response({'Not implemented', 'TODO'})