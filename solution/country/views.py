from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import status
from core.exceptions import ReasonException
from country.models import Country
from country.serializers import CountrySerializer

from rest_framework.views import exception_handler
# Create your views here.
class CountryListView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        regions = self.request.query_params.getlist('region')
        valid_regions = self.serializer_class.Meta.model.valid_regions

        if regions:
            for region in regions:
                if region not in valid_regions:
                    raise ReasonException(reason='Not valid region.', status_code=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.filter(region__in=regions)

        return queryset.order_by('alpha2')

class CountryView(RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'alpha2'
    lookup_url_kwarg = 'alpha2'