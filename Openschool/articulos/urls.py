from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'articulos'

urlpatterns = [
    path('', views.index, name='index'),
    path('preguntas/<int:Carrera>', views.detail, name='detail'),
    path('CrearPregunta/<int:Materiaid>/', views.ArticuloFormA, name='ArticuloFormA'),
    path('<int:Preguntaid>/results/', views.results, name='results'),
    path('<int:Preguntaid>/results/<int:Comentariosid>', views.resultsH, name='resultsH'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
