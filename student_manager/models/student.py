from odoo import fields, models, api


class Student(models.Model):
    _name = "student.student"
    _description = "Student"

    name = fields.Char(string="Name", required=True)
    age = fields.Integer(string="Age")
    address = fields.Char(string="Address")
    sex = fields.Selection([
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ], string="Sex")
    email = fields.Char(string="Email")
    note = fields.Text(string="Note")
    user_id = fields.Many2one("res.users", string="User", default=lambda self: self.env.user)

    _sql_constraints = [
        ("email_unique", "unique(email)", "Email must be unique"),
    ]
