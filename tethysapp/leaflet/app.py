from tethys_sdk.base import TethysAppBase, url_map_maker


class Leaflet(TethysAppBase):
    """
    Tethys app class for Leaflet.
    """

    name = 'Leaflet'
    index = 'leaflet:home'
    icon = 'leaflet/images/icon.gif'
    package = 'leaflet'
    root_url = 'leaflet'
    color = '#16a085'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='leaflet',
                controller='leaflet.controllers.home'
            ),
        )

        return url_maps