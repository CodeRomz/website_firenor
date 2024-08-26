from odoo import _, api, fields, models

class FN_Channel(models.Model):
    _inherit = 'slide.channel'

    def _default_cover_properties(self):
        """Override the default cover properties to change the background image gradient."""
        res = super(FN_Channel, self)._default_cover_properties()
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
