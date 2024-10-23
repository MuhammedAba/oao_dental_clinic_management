{
    'name': 'Dental Clinic Management',
    'version': '16.0.0.0.1',
    'category': 'Healthcare',
    'summary': 'Dental clinic management system for dentists',
    'description': """
        OAO Dental Clinic Management
        ============================
        This module helps dentists manage their clinic activities, including patient records, appointments, treatments, and billing.
    """,
    'author': 'ABA TECH GROUP',
    'website': 'https://omeraba.com/tr/blog/odoo-projeleri-23/dis-klinigi-yonetim-sistemi-48',
    'depends': ['base', ],
    'data': [
        'views/patient_views.xml',
        'views/employee_type_views.xml',
        'security/ir.model.access.csv',
        'data/employee.type.csv',
    ],
    # 'images': ['static/src/description/icon.png'],
    'sequence': '-1',
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
