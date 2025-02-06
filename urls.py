# cable_tracer/urls.py
from django.urls import path, include
from . import views
from .api.urls import urlpatterns as api_urls

urlpatterns = [
    # Маршруты для веб-интерфейса
    path('', views.CableTraceListView.as_view(), name='cabletrace_list'),  # Список трассировок
    path('add/', views.CableTraceEditView.as_view(), name='cabletrace_add'),  # Добавление новой трассировки
    path('<int:pk>/', views.CableTraceView.as_view(), name='cabletrace'),  # Просмотр конкретной трассировки
    path('<int:pk>/edit/', views.CableTraceEditView.as_view(), name='cabletrace_edit'),  # Редактирование трассировки
    path('<int:pk>/delete/', views.CableTraceDeleteView.as_view(), name='cabletrace_delete'),  # Удаление трассировки
# Маршруты для API
    path('api/', include(api_urls)),
]
