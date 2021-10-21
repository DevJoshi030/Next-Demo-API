from django.urls import path

from .views import CampaignViewset, SubscriberViewset

urlpatterns = [
    path('campaigns/', CampaignViewset.as_view({
        'get': 'get_all_campaigns',
        'post': 'create_campaign',
    })),
    path('id/<str:campaign_slug>/', CampaignViewset.as_view({
        'get': 'get_id_from_slug'
    })),
    path('campaigns/<str:campaign_slug>/', CampaignViewset.as_view({
        'get': 'get_single_campaign'
    })),
    path('subscribers/', SubscriberViewset.as_view({
        'get': 'get_all_subscribers',
        'post': 'create_subscriber',
    })),
]
