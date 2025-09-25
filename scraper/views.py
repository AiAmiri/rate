from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from .models import KhorasanRate, SaraiRate, DaAfgRate
from .serializers import KhorasanRateSerializer, SaraiRateSerializer, DaAfgRateSerializer
from .utils import scrape_rates as run_scrape
from rest_framework.decorators import api_view, permission_classes

class KhorasanRatesAPIView(APIView):
    permission_classes = [HasAPIKey]
    def get(self, request):
        khorasan_rates = KhorasanRate.objects.all()
        data = {
            "khorasan_rates": KhorasanRateSerializer(khorasan_rates, many=True).data,
        }
        return Response(data)


class SaraiRatesAPIView(APIView):
    permission_classes = [HasAPIKey]
    def get(self, request):
        sarai_rates = SaraiRate.objects.all()
        data = {
            "sarai_rates": SaraiRateSerializer(sarai_rates, many=True).data,
        }
        return Response(data)

class DaAfgRatesAPIView(APIView):
    permission_classes = [HasAPIKey]

    def get(self, request):
        da_afg_rates = DaAfgRate.objects.all()
        data = {
            "da_afg_rates": DaAfgRateSerializer(da_afg_rates, many=True).data,
        }
        return Response(data)
        

@api_view(['POST'])
@permission_classes([HasAPIKey])
def scrape_rates(request):
    """
    Trigger scraping of rates from configured sources.
    Returns a simple status payload. Authentication enforced by global DRF settings.
    """
    run_scrape()
    return Response({"status": "ok"})