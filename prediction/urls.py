from django.urls import path
from . import views

urlpatterns = [
    path('streamlit/', views.streamlit_app, name='streamlit_app'),
]