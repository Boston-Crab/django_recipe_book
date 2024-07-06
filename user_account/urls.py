from django.urls import path
from user_account.views import (
    user_login,
    user_signup,
    user_logout, 
    user_account,
    user_change_password,
    user_email_change,
)

app_name = "user"

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', user_signup, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('account/', user_account, name='account'),
    path('change-password/', user_change_password, name='change_password'),
    path('change-email', user_email_change, name='change_email'),
]
