from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('specialty/',views.skills_1,name="skills-1"),
    path('passion/',views.skills_2,name="skills-2"),
    path('talents/',views.skills_3,name="skills-3"),

    # path('',views.theme_switch,name="switch_theme"),
    # path("__reload__/", include("django_browser_reload.urls")),
]

