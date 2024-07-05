from django.urls import path
from user_account.views import user_login, user_signup, user_logout

app_name = "user"

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
]
