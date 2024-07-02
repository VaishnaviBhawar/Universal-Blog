from django.contrib import admin
from . import views
from django.urls import path, include


from .views import Dashboard,AddCommentView,LikeView,CategoryListView, CategoryView, AddCategoryView, HomeView, ArticleDetailView, AddPostView, \
    UpdatePostView, DeletePostView

urlpatterns = [
    # path('',views.home,name='home'),
    path('', Dashboard, name='dashboard'),
    path('home/', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('category-list/', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),

]
