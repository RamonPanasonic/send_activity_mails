from odoo import models, fields, api
from datetime import date

class CrmActivityReportScheduler(models.Model):
    _name = 'crm.activity.report.scheduler'
    _description = 'Scheduled Email for CRM Call Activities'

    def send_crm_call_activity_report(self):
        """ today = fields.Date.context_today(self)
        domain = [('mail_activity_type_id', '=', 2), ('activity_date', '=', today)]
        
        activities = self.env['crm.activity.report'].read_group(
            domain=domain,
            fields=['user_id', 'activity_type_id:count(activity_type_id)'],
            groupby=['user_id']
        )

        if activities:
            report_lines = [
                f"{activity.get('user_id', [''])[1]}: {activity.get('activity_type_id_count', 0)}"
                for activity in activities
            ]
            body_html = "<h3>CRM Call Activities Report</h3><ul>"
            body_html += ''.join(f"<li>{line}</li>" for line in report_lines)
            body_html += "</ul>" """
        
        cantidad_gibran = self.env['crm.activity.report'].search_count(["&", ("mail_activity_type_id", "=", 2), ("user_id", "=", 24)])

        body_html = ""

        if cantidad_gibran:
            body_html += "<h3>Gibran: " + str(cantidad_gibran) + "</h3><br/>"

        mail_values = {
            'subject': 'Reporte de llamadas de vendedores',
            'body_html': body_html,
            'email_to': 'ramon@industrialpanasonic.com',
            'email_from': self.env.user.company_id.email or self.env.user.email,
        }
        self.env['mail.mail'].create(mail_values).send()