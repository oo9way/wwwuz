from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from app.models import Website, Visitor, Data
from datetime import datetime
from rest_framework.generics import ListAPIView
from api.serializers import WebsiteSerializer, DataSerializer
from django.utils.translation import gettext as _

@api_view(['POST'])
def add_count(request):
    today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

    try:
        api_key = request.POST['api_key']
        visitor_hash = request.POST['user_hash']
    except:
        return Response(data={"message":_("Credentals are not provided")}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        website = Website.objects.get(api_key=api_key)
    except:
        return Response(data={"message":_("Website not found")}, status=status.HTTP_404_NOT_FOUND)
    
    try:
        data = Data.objects.filter(website=website, date__gte=today)[0]
            
    except:
        data = Data(website=website, date=today)
        data.save()

    try:
        visitor = Visitor.objects.get(visitor_hash=visitor_hash, website=website)
        data.visitors += 1
    except:
        visitor = Visitor(visitor_hash=visitor_hash, website=website)
        visitor.save()
        data.unique_visitors += 1
        data.visitors += 1

    data.save()

    return Response(data={"message":_("Added successfuly")}, status=status.HTTP_200_OK)


class WebsiteListAPIView(ListAPIView):
    queryset = Website.objects.select_related('owner', 'category')
    serializer_class = WebsiteSerializer

class DataListAPIView(ListAPIView):
    queryset = Data.objects.select_related('owner', 'category')
    serializer_class = DataSerializer