from django.conf.urls import url
from tutoring.views import OrderView

urlpatterns = [
    url(r'^(?P<id>\d+)', OrderView.as_view(), name='order_url'),
]
