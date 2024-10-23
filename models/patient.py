from odoo import api, fields, models
from datetime import date, timedelta


class Patient(models.Model):
    _name = "patient.patient"
    _description = "Patients"
    _order = 'name desc'

    name = fields.Char(string="Patient Name", required=1)
    surname = fields.Char(string="Patient Surname", required=1)
    date_of_birth = fields.Date(string='Date Of Birth', default=date.today(), required=1)
    age = fields.Char(string='Age In Years', compute="compute_age", store=True)
    image = fields.Image(string="Image")
    gender = fields.Selection([('male', "Male"), ('female', 'Female')], string='Gender', default='male')
    note = fields.Text(string="Description")
    phone = fields.Char(string="Phone", required=1)
    email = fields.Char(string="Email")
    blood_type = fields.Selection([
        ('a-', 'A without Rh-factor'),
        ('a+', 'A with Rh-factor'),
        ('b-', 'B without Rh-factor'),
        ('b+', 'B with Rh-factor'),
    ], string="Blood Typing", required=1)

    @api.depends('date_of_birth')
    def compute_age(self):
        if self.date_of_birth:
            today = fields.Date.today()
            age = today - self.date_of_birth
            age_in_years = age.days // 365.25
            self.age = f"{int(age_in_years)} Years Old"
        else:
            self.age = "No Date of Birth"