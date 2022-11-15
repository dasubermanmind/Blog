from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # GET->
    path('', views.post_list, name='post_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
    # GET ->
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
    # POST-> Share post via email medium
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    # POST -> comment
    path('<int:post_id>/comment/', views.post_comment, name='post_comment'),
    # GET-> Only renders html
    path('about/', views.about_me, name='about_me'),
    # Posts by tag
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag')
]
