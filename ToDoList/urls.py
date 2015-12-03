from django.conf.urls import url
from views import *

urlpatterns = [
    url(r'^$', empty_page, {'template':'home_page.html'}),
    url(r'^my_todo_list/$', todo_list, {'template':'to_do_list_page.html'}),
    url(r'^redact/(\d+)/$', edit_text, {'template':'redact_page.html'}),

    url(r'^registration_ty/$', empty_page, {'template':'congratulate.html'}),
    url(r'^registration/$', registration, {'template':'registration_page.html'}),
    url(r'^signin/$', signin, {'template':'signin_page.html'}),
    url(r'^signout/$', signout),

    url(r'^delete/(?P<id>\d+)/$', action, {'action_type': 'delete'}),
    url(r'^done/(?P<id>\d+)/$', action, {'action_type': 'done'}),
    url(r'^undone/(?P<id>\d+)/$', action, {'action_type': 'undone'}),
    url(r'^in_progress/(?P<id>\d+)/$', action, {'action_type': 'in_progress'}),
]