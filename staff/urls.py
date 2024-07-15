from django.urls import path, include

from staff.views import DetailByConditionView

urlpatterns = [
    path('staff', DetailByConditionView.as_view())
]
