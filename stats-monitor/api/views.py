from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ResponseLogSerializer
from collector.models import ResponseLog


@api_view(('GET'))
def FullLog(request):
    """
    Retrieves all URL queries
    """
    if request.method == 'GET':
        data = ResponseLog.objects.all()
        serializer = ResponseLogSerializer(data, many=True)
        return Response(serializer.data)
