# -*- coding: utf-8 -*-
"""
Feed renderers (to work with django_feedparser)
"""
from django_feedparser.renderer import FeedBasicRenderer
from django.template.loader import render_to_string

class SafeRenderer(FeedBasicRenderer):
    """
    Overrides renderer method of FeedBasicRender with safe version which fails more gracefully
    TODO: doesn't solve problem properly yet
    
    """
    
    def render(self, url, template=None, expiration=0):
        """
        Render feed template
        """
        template = template or self.default_template
        
        try:
            return render_to_string(template, self.get_context(url, expiration))
        except:
            return "ERROR retrieving feed"