from django.urls import re_path,path
from owner.views import OwnerView

urlpatterns = [
    path('owner/',OwnerView.as_view())
]
