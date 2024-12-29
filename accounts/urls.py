from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path("password/change/", views.PasswordChangeView.as_view(), name="password_change"),
    path("password/change/done/", views.PasswordChangeDoneView.as_view(), name="password_change_done", ),
    path("password/reset/", views.PasswordResetView.as_view(), name="password_reset"),
    path("password/reset/done/", views.PasswordResetDoneView.as_view(), name="password_reset_done", ),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm", ),
    path("reset/done/", views.PasswordResetCompleteView.as_view(), name="password_reset_complete", ),
    # path("settings/users/update/<int:pk>", views.UserUpdateWithAdmin.as_view(), name='user_update_admin'),
    # path("settings/users/delete/<int:pk>", views.UserDeleteView.as_view(), name='user_delete'),
    # path("users/update/<int:pk>", views.UserUpdate.as_view(), name='user_update'),
    # path("users/create/", views.UserCreate.as_view(), name='user_create'),
    # path("users/", views.UsersList.as_view(), name='users_list'),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path('login/', views.LoginView.as_view(), name='login'),
    path("", views.DashboardView.as_view(), name="dashboard"),
]
