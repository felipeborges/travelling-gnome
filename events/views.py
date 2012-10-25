from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext

from events.models import Event

def event_page(request, event_slug):
    event = get_object_or_404(Event, slug = event_slug)

    return render_to_response('events/event_page.html', {
                              'event' : event, 
                            }, RequestContext(request))