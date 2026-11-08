from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'  # اسم الجدول في قاعدة البيانات (سيكون todo_task)
    _description = 'قائمة المهام اليومية'

    name = fields.Char(string='عنوان المهمة', required=True)
    description = fields.Text(string='تفاصيل المهمة')
    is_completed = fields.Boolean(string='تم الإنجاز؟', default=False)
    deadline = fields.Date(string='تاريخ الانتهاء')
