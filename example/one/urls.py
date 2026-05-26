
from django.urls import path
from .views import detailed,detailedview

urlpatterns = [
    
    path('detail/',detailed.as_view() ),
    path('detail<int:pk>/',detailedview.as_view() ),
    
]