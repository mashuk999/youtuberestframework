from django.contrib.syndication.views import Feed
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import redirect
from django.template.defaultfilters import truncatewords
from .models import SaveVideo
from django.urls import reverse
from django.http import HttpResponse, JsonResponse


class Videofeed(Feed):
    title = "My blog"
    link = ""
    description = "New posts of my blog."

    def items(self):
        return SaveVideo.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.videoPublicId

    def item_link(self, item):
        # return 'http://lit-sierra-15246.herokuapp.com/download?urlpath='+str(item.video)
        return item.videoUrl

    # Only needed if the model has no get_absolute_url method
    # def item_link(self, item):
    #     return reverse("post_detail", args=[item.slug])