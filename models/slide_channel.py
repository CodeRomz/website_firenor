from odoo import _, api, fields, models

class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    def _default_cover_properties(self):
        """Override the default cover properties to change the background image gradient."""
        res = super()._default_cover_properties()  # Correct class name here
        # Update the background image with the new gradient
        res.update({
            "background_color_class": "o_cc3",
            'background_color_style': (
                'background-color: rgba(0, 0, 0, 0); '
                'background-image: linear-gradient(120deg, #47a5ae, #47a5ae) !important;'
            ),
            'opacity': '0',
            'resize_class': 'cover_auto'
        })
        return res

    # Override default_get method to set default values
    # @api.model
    # def default_get(self, fields_list):
    #     res = super(SlideChannel, self).default_get(fields_list)
    #     # Use _default_cover_properties to set default cover values
    #     cover_defaults = self._default_cover_properties()
    #     res.update(cover_defaults)  # Update the defaults
    #     return res


# i notice the defalut is this (res = super()._default_cover_properties()) and you change it to this (res = super(SlideChannel, self)._default_cover_properties() ) can you explain?
