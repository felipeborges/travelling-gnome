from django.db import models
from django.utils.translation import ugettext_lazy as _

class Event(models.Model):
    title = models.CharField(_('name'), max_length = 250)
    description = models.TextField(_('details'))

    slug = models.SlugField(unique = True)

    start_time = models.DateTimeField(_('start time'), blank = True, null = True)
    end_time = models.DateTimeField(_('end time'), blank = True, null = True)

    location = models.CharField(_('where'), max_length = 300, blank = True, null = True)

    def __unicode__(self):
        return _("%(title)s on %(start)s ~ %(end)s") % { 'title' : self.title,
                                                         'start' : self.start_time,
                                                         'end'   : self.end_time }