from django.urls import path

from . import views
app_name = 'foro'

urlpatterns = [
    path('', views.index, name='index'),
    path('preguntas/<int:Carrera>', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:Preguntaid>/results/<int:Comentariosid>', views.resultsH, name='resultsH'),
    path('<int:Preguntaid>/results/', views.results, name='results'),
    path('CrearPregunta/<int:Materiaid>/', views.PreguntaFormA, name='PreguntaFormA'),
    path('buscar',views.Buscar,name='buscar'),
]
