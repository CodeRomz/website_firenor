from odoo import _, api, fields, models

class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    def _default_cover_properties(self):
        """Override the default cover properties to change the background image gradient."""
        res = super()._default_cover_properties()
        # Update the background image with the new gradient
        res.update({
            'header_text_color_style':'color: white !important;',
            'background_color_style': (
                'background-image: linear-gradient(120deg, #47a5ae, #47a5ae) !important;'
            ),
        })
        return res