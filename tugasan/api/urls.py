from django.urls import path
from . import apiviews

app_name = 'tugasan'

urlpatterns = [
    # path("login/", LoginView.as_view(), name="login"),
    # path("users/", UserCreate.as_view(), name="user_create"),
    # path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="polls_list"),
    # path(
    #     "polls/<int:pk>/choices/<int:choice_pk>/vote/",
    #     CreateVote.as_view(),
    #     name="polls_list",
    # ),
    path('', apiviews.index, name="tugasan-api-index"),
    path('test/appdata', apiviews.apiappdata, name="tugasan-api-appdata"),
    path('tobuy/create', apiviews.save_untuk_beli, name="tugasan-api-save-beli"),
    path('tobuy/list', apiviews.list_untuk_beli, name="tugasan-api-list-beli"),
    path('tobuy/edit/<int:pk>', apiviews.edit_untuk_beli, name="tugasan-api-edit-beli"),
    path('tobuy/delete/<int:pk>', apiviews.delete_untuk_beli, name="tugasan-api-delete-beli"),
    path('tobuy/', apiviews.untuk_beli, name="tugasan-api-beli"),
    # path('home/cubaan/', views.cubaan, name="home-cubaan"),

]
    

