from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from django.template.defaultfilters import slugify

from .models import Campaign, Subscriber
from .serializers import CampaignSerializer, SubscriberSerializer
# Create your views here.


class CampaignViewset(ViewSet):

    def get_all_campaigns(self, request: Request) -> Response:

        campaigns = Campaign.objects.all()
        serializer = CampaignSerializer(campaigns, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_single_campaign(self, request: Request, campaign_slug: str) -> Response:

        try:
            campaign = Campaign.objects.get(slug=campaign_slug)
        except Campaign.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = CampaignSerializer(campaign)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_id_from_slug(self, request: Request, campaign_slug: str) -> Response:

        try:
            campaign = Campaign.objects.get(slug=campaign_slug)
        except Campaign.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(campaign.id, status=status.HTTP_200_OK)

    def create_campaign(self, request: Request) -> Response:

        serailizer = CampaignSerializer(data=request.data)
        serailizer.is_valid(raise_exception=True)

        title = serailizer.validated_data.get('title')
        description = serailizer.validated_data.get('description')
        logo = serailizer.validated_data.get('logo')

        to_assign = slugify(title)

        filtered_campaigns = Campaign.objects.filter(slug=to_assign)

        if filtered_campaigns.exists():
            to_assign = to_assign + f"-{filtered_campaigns.count()}"

        Campaign.objects.create(
            title=title, description=description, slug=to_assign, logo=logo)

        return Response(status=status.HTTP_201_CREATED)


class SubscriberViewset(ViewSet):

    def get_all_subscribers(self, request: Request) -> Response:

        subscribers = Subscriber.objects.all()
        serializer = SubscriberSerializer(subscribers, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_subscriber(self, request: Request) -> Response:

        serailizer = SubscriberSerializer(data=request.data)
        serailizer.is_valid(raise_exception=True)

        email = serailizer.validated_data.get('email')
        campaign = serailizer.validated_data.get('campaign')

        try:
            Campaign.objects.get(slug=campaign.slug)

        except Campaign.DoesNotExist:

            return Response(status=status.HTTP_404_NOT_FOUND)

        finally:
            Subscriber.objects.create(email=email, campaign=campaign)

        return Response(status=status.HTTP_201_CREATED)
