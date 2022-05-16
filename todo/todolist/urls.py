from django.urls import path
from .views import HomePage, HomePageDetails, TaskCreate, TaskDelete, TaskUpdate, SignIn, RegisterPage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', SignIn.as_view(),  name='sign-in'),
    path('logout/', LogoutView.as_view(next_page='sign-in'), name='sign-out'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('', HomePage.as_view(),  name='task'),
    path('task/<int:pk>/', HomePageDetails.as_view(),  name='task-detail'),
    path('task-create', TaskCreate.as_view(),  name='task-create'),
    path('task-update/<int:pk>/',TaskUpdate.as_view(),  name='task-update'),
    path('task-delete/<int:pk>/',TaskDelete.as_view(),  name='task-delete'),
]
