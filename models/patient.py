from odoo import api, fields, models
from datetime import date, timedelta


class Patient(models.Model):
    _name = "patient.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Patients"
    _order = 'name desc'

    patient_id = fields.Char(string="Patient ID", readonly=True, copy=False, default="New Patient")
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
    active = fields.Boolean(string="Active", default=True)

    @api.depends('date_of_birth')
    def compute_age(self):
        if self.date_of_birth:
            today = fields.Date.today()
            age = today - self.date_of_birth
            age_in_years = age.days // 365.25
            self.age = f"{int(age_in_years)} Years Old"
        else:
            self.age = "No Date of Birth"

    @api.model
    def create(self, vals):
        # Eğer patient_id boşsa
        if not vals.get('patient_id'):
            # SQL ile mevcut en yüksek patient_id'yi alıyoruz
            self._cr.execute(
                "SELECT COALESCE(MAX(CAST(SUBSTRING(patient_id, 4, LENGTH(patient_id)) AS INTEGER)), 0) FROM patient_patient")
            max_id = self._cr.fetchone()[0]

            # Yeni patient_id'yi oluşturuyoruz
            new_id = max_id + 1
            vals['patient_id'] = f'PAT{str(new_id).zfill(5)}'  # PAT00001 gibi

        return super(Patient, self).create(vals)
