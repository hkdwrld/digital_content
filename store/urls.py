from django.urls import path
from .views import home,auto_complete

urlpatterns = [
    path('', home, name="home"),
    path('autocomplete',auto_complete,name='auto-complete')

]
