from django.urls import path
from . import views
app_name='myapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('enter_recipe/',views.enter_recipe,name='enter_recipe'),
    path('comment/',views.comment, name='comment'),
    path('save_comment/<int:id>/',views.save_comment,name='save_comment')
]