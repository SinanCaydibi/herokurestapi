from rest_framework.generics import ListAPIView , CreateAPIView ,RetrieveUpdateAPIView
from api.models import Data
from .serializers import OksiSerializer,OksiUpdateCreateSerializer
class ExampleListAPIView(ListAPIView):
    queryset = Data.objects.all()
    serializer_class = OksiSerializer


class ExampleCreateAPIView(CreateAPIView) :
    queryset = Data.objects.all()
    serializer_class = OksiSerializer

class ExampleUpdateAPIView(RetrieveUpdateAPIView) :
    queryset = Data.objects.all()
    serializer_class = OksiUpdateCreateSerializer
    lookup_field='slug'
    def perfom_update(self,serializer):
        serializer.save()
