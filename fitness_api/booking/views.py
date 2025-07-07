from rest_framework.views import APIView
from rest_framework.response import Response

class FitnessClassListView(APIView):

    def get(self, request):
        return Response({"message": "List all fitness classes"})
