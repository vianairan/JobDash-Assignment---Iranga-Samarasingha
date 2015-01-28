from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ToDo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^todo_app/', include('todo_app.urls', namespace="todo_app")),
    url(r'^admin/', include(admin.site.urls)),
)
