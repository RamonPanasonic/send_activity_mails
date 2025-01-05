from odoo import models, fields, api
from datetime import date

class CrmActivityReportScheduler(models.Model):
    _name = 'crm.activity.report.scheduler'
    _description = 'Scheduled Email for CRM Call Activities'

    def send_crm_call_activity_report(self):
        """Send an email with the count of call activities grouped by salesperson."""
        today = date.today()
        domain = [('mail_activity_type_id', '=', 2), ('activity_date', '=', today)]
        activities = self.env['crm.activity.report'].read_group(
            domain=domain,
            fields=['user_id', 'activity_type_id:count(activity_type_id)'],
            groupby=['user_id']
        )

        if activities:
            report_lines = [
                f"{activity['user_id'][1]}: {activity['activity_type_id_count']}"
                for activity in activities
            ]
            body_html = "<h3>CRM Call Activities Report</h3><ul>"
            body_html += ''.join(f"<li>{line}</li>" for line in report_lines)
            body_html += "</ul>"

            mail_values = {
                'subject': 'Daily CRM Call Activities Report',
                'body_html': body_html,
                'email_to': 'ramon@industrialpanasonic.com',  # Cambia al destinatario real
                'email_from': '{{ (object.company_id.email_formatted or user.email_formatted) }}',
            }
            self.env['mail.mail'].create(mail_values).send()
