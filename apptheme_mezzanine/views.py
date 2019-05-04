from mezzanine_agenda.feeds import EventsAtom
from feeds import EventsRSS
from django.http import Http404
#from django.http import HttpResponse, HttpResponseNotFound

#def event_feed(request, format):
#    # ...
#    return HttpResponse('<h1>Test Page: %s</h1>' % format)

def event_feed(request, format, **kwargs):
    """
    Events feeds - maps format to the correct feed view.
    """
    try:
        return {"rss": EventsRSS, "atom": EventsAtom}[format](**kwargs)(request)
    except KeyError:
        raise Http404()