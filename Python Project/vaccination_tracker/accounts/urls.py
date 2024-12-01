from django.urls import path
from .views import parent_signup, facilitator_signup, login_view
from .views import register_child

app_name = 'accounts' 

urlpatterns = [
    path('signup/parent/', parent_signup, name='parent_signup'),
    path('signup/facilitator/', facilitator_signup, name='facilitator_signup'),
    path('login/', login_view, name='login'),  # Add this line for the login URL
    path('register/child/', register_child, name='register_child'),
]
