from django.shortcuts import render

def streamlit_app(request):
    return render(request, 'streamlit_app.html')
