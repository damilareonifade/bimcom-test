from django.urls import path
from . import views

app_name='polling'

urlpatterns = [
    path('polling-unit-results/',views.result_polling_unit,name='polling_unit_result'),
    path('polling-result-create/',views.polling_result_create,name='polling_result_create')
]
