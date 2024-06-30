from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.views import AccountViewSet
from destinations.views import DestinationViewSet, IncomingDataView

router = DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'destinations', DestinationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('server/incoming_data/', IncomingDataView.as_view(), name='incoming-data'),
]
