from odoo import models, fields, api


class HostelRoom(models.Model):
    _name="hostel.room"
    _description="Hostel Room"

    name = fields.Char(string="Room Name", required=True)
    description = fields.Text(string="Description")
    room_number = fields.Char(string="Room Number", required=True)
    floor = fields.Integer(string="Floor")
    capacity = fields.Integer(string="Capacity")
    room_type = fields.Selection([('single', 'Single'), ('double', 'Double'), ('triple', 'Triple')], string="Room Type")
    image = fields.Binary(string="Image")
    active = fields.Boolean(string="Active", default=True)
    hostel_id = fields.Many2one(comodel_name="hostel.hostel", string="Hostel")
    currency_id = fields.Many2one(comodel_name="res.currency", string="Currency")
    #hostel_currency = fields.Many2one(comodel_name="res.currency", string="Currency", currency_field='currency_id')
    #optional attribute: currency_field = 'currency_id' incase currency field have another name then 'currency_id'
    rent_amount = fields.Monetary('Rent Amount', help="Enter rent amount per month")
    student_ids = fields.One2many(comodel_name="hostel.student", inverse_name="room_id", string="Students")
    hostel_amenities_ids = fields.Many2many("hostel.amenities","hostel_room_amenities_rel", "room_id", "amenity_id", string="Amenities", domain="[('active', '=', True)]", help="Select hostel room amenities")