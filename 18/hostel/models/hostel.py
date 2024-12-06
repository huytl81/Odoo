# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Hostel(models.Model):
    _name = 'hostel.hostel'
    _description = "Information about hostel"
    _order = "id desc, name"
    _rec_name = 'hostel_code'
    _rec_names_search = ['name', 'hostel_code', 'email', 'mobile'] #similar to using the name_search function.

    name = fields.Char(string="Hostel Name", required=True)
    hostel_code = fields.Char(string="Hostel Code", required=True)
    street = fields.Char('Street', required=True)
    street2 = fields.Char('Street2')
    zip = fields.Char('Zip', change_default=True)
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    phone = fields.Char('Phone', required=True)
    mobile = fields.Char('Mobile', required=True)
    email = fields.Char('Email')
    hostel_floors = fields.Integer(string="Total Floors")
    image = fields.Binary('Hostel Image')
    active = fields.Boolean("Active", default=True, help="Activate/Deactivate hostel record")
    type = fields.Selection([("male", "Boys"), ("female","Girls"),("common", "Common")], "Type", help="Type of Hostel",required=True, default="common")
    other_info = fields.Text("Other Information", help="Enter more information")
    description = fields.Html('Description')
    #hostel_rating = fields.Float('Hostel Average Rating',digits=(14, 4)) # Method 1: Optional precision (total,decimals)
    hostel_rating = fields.Float('Hostel Average Rating', digits = 'Rating Value')  # Method 2
    hostel_room_ids = fields.One2many('hostel.room',  inverse_name='hostel_id', string="Rooms")


    @api.depends('hostel_code')
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.hostel_code:
                name = f'{name} ({record.hostel_code})'
            record.display_name = name
