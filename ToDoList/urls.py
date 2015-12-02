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

    url(r'^delete/(\d+)/$', delete_action),
    url(r'^done/(\d+)/$', done_action),
    url(r'^undone/(\d+)/$', undone_action),
    url(r'^in_progress/(\d+)/$', in_progress_action),
]