from django.contrib.syndication.views import Feed
from .models import SaveVideo_entertainment


class Videofeed(Feed):
    title = "My blog"
    link = ""
    description = "New posts of my blog."

    def items(self):
        return SaveVideo_entertainment.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.title

    def item_link(self, item):
        # return 'http://lit-sierra-15246.herokuapp.com/download?urlpath='+str(item.video)
        return item.videoUrl

    # Only needed if the model has no get_absolute_url method
    # def item_link(self, item):
    #     return reverse("post_detail", args=[item.slug])