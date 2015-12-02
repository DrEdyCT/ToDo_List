from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', home_page),
    url(r'^my_todo_list/$', todo_list),
    url(r'^redact/(\d+)/$', edit_text),

    url(r'^registration/$', registration),
    url(r'^signin/$', signin),
    url(r'^signout/$', signout),
    url(r'^to_do_list/$', go_to_todo_list),

    url(r'^delete/(?P<id>\d+)/$', action, {'action_type': 'delete'}),
    url(r'^done/(?P<id>\d+)/$', action, {'action_type': 'done'}),
    url(r'^undone/(?P<id>\d+)/$', action, {'action_type': 'undone'}),
    url(r'^in_progress/(?P<id>\d+)/$', action, {'action_type': 'in_progress'}),
]