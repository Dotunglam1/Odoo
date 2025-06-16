from odoo import http
from odoo.http import request


class StudentController(http.Controller):
    @http.route('/students', type='http', auth='user', website=True)
    def list_students(self, **kwargs):
        students = request.env['student.student'].sudo().search([])
        return request.render('student_manager.students_page', {
            'students': students,
        })
