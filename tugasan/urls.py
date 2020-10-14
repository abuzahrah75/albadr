from django.urls import path
from . import views
# from .apiviews import api_untuk_beli


# from rest_framework.routers import DefaultRouter
# from rest_framework.documentation import include_docs_urls

# app_name = 'tugasan'

# router = DefaultRouter()
# router.register("polls", PollViewSet, base_name="polls")

# router = DefaultRouter()
# router.register("api/appdata", views.apiappdata, basename="tugasan")


urlpatterns = [
    # path("login/", LoginView.as_view(), name="login"),
    # path("users/", UserCreate.as_view(), name="user_create"),
    # path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="polls_list"),
    # path(
    #     "polls/<int:pk>/choices/<int:choice_pk>/vote/",
    #     CreateVote.as_view(),
    #     name="polls_list",
    # ),
    path('', views.index, name="tugasan-index"),
    path('api/appdata', views.apiappdata, name="tugasan-api-appdata"),
    # path('home/cubaan/', views.cubaan, name="home-cubaan"),

]
    


# urlpatterns += router.urls




# urlpatterns = [
#     path("login/", LoginView.as_view(), name="login"),
#     path("users/", UserCreate.as_view(), name="user_create"),
#     path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="polls_list"),
#     path(
#         "polls/<int:pk>/choices/<int:choice_pk>/vote/",
#         CreateVote.as_view(),
#         name="polls_list",
#     ),

    
# ]

# urlpatterns += router.urls
