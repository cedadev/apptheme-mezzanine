from __future__ import unicode_literals

from django.conf.urls import url

from . import views
from mezzanine.conf import settings


# Trailing slash for urlpatterns based on setup.
_slash = "/" if settings.APPEND_SLASH else ""

# patterns
urlpatterns = [
    url("^/events/feeds/(?P<format>.*)%s$" % _slash,
        views.event_feed, name="event_feed"),
]
