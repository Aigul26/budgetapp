from django.urls import path
from .views import ProjectDetailAPIView, ProjectListAPIView, ExpenseDetailAPIView, ExpenseListAPIView, IncomeListAPIView
from .import views


urlpatterns = [
    path('', ProjectListAPIView.as_view()),
    path('<int:id>/', ProjectDetailAPIView.as_view()),
    path('income/<int:id>/', IncomeListAPIView.as_view()),
    path('chernovik/', views.chernovik, name='chernovik'),

    #path('expense/<int:id>/', ExpenseDetailAPIView.as_view()),
    ]