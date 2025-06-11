from django.urls import path
from .import views

urlpatterns = [
    path("process/", views.payment_process, name="process"),
    path("payment-session/", views.payment_session, name="payment_session"),
    path("cancel/", views.cancel, name="cancel"),
    path("fail/", views.fail, name="fail"),
    path("success/", views.success, name="success"),
    path("complete/", views.complete, name="complete"),
    path("purchase/<str:val_id>/<str:trans_id>/", views.shopping, name="shopping"),
    
]
