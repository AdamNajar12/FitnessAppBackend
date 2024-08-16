from django.urls import path

from .views import( UserView, CoachView, ClientView, login, GetCurrentUserView,SomeProtectedView,logout)
from rest_framework_simplejwt.views import TokenRefreshView 




urlpatterns = [
    path('register/user/', UserView.as_view(), name='register_user'),
    path('register/coach/', CoachView.as_view(), name='register_coach'),
    path('register/client/', ClientView.as_view(), name='register_client'),
   # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('login/', login, name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Utilisez cette ligne
    path('current-user/', GetCurrentUserView.as_view(), name='current_user'),
    path('getUser',SomeProtectedView.as_view()),
    path('logout',logout,name='logout')
]

    

