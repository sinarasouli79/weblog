# The views used below are normally mapped in the AdminSite instance.
# This URLs file is used to provide a reliable view deployment for test purposes.
# It is also provided as a convenience to those who want to deploy these URLs
# elsewhere.

from django.contrib.auth import views
from django.urls import path

from .views import (ArticleDelete, CreateArticle, Home, LoginView,
                    PasswordChangeView, Profile, UpdateArticle)

app_name = 'account'
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path(
        "password_change/",
        PasswordChangeView.as_view(
            template_name='registration/account_password_change_form.html'),
        name="password_change"
    ),
    path(
        "password_change/done/",
        views.PasswordChangeDoneView.as_view(
            template_name='registration/account_password_change_done.html'),
        name="password_change_done",
    ),
    # path("password_reset/", views.PasswordResetView.as_view(), name="password_reset"),
    # path(
    #     "password_reset/done/",
    #     views.PasswordResetDoneView.as_view(),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     views.PasswordResetConfirmView.as_view(),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset/done/",
    #     views.PasswordResetCompleteView.as_view(),
    #     name="password_reset_complete",
    # ),
]

urlpatterns += [
    path('home/', Home.as_view(), name='home'),
    path('create/', CreateArticle.as_view(), name='create-article'),
    path('update/<int:pk>/', UpdateArticle.as_view(), name='update-article'),
    path('delete/<int:pk>/', ArticleDelete.as_view(), name='delete-article'),
    path('profile/', Profile.as_view(), name='profile'),
]
