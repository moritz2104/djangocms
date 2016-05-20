from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _
from polls_plugin.cms_menus import PollsMenu

class PollsApphook(CMSApp):
    name = _("Polls Application")   # give your application a name (required)
    urls = ["polls.urls"]           # link your app to url configuration(s)
    app_name = "polls"
    menus = [PollsMenu]


apphook_pool.register(PollsApphook)  # register the application