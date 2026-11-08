{
    'name': 'إدارة المهام اليومية (To-Do)',
    'version': '1.0',
    'summary': 'موديول بسيط لإنشاء ومتابعة المهام اليومية لمبرمجي أودو',
    'category': 'Tools',
    'author': 'اسمك كمطور بايثون',
    'depends': ['base'],  # يعتمد على النظام الأساسي لأودو
    'data': [
        'views/todo_task_view.xml',  # ملف الواجهات وتصميم الشاشات
    ],    
    'demo': [
        'data/todo_task_demo.xml',  # هنا نقوم باستدعاء الـ Dataset التجريبية
    ],

     
    'installable': True,
    'application': True,  # ليظهر كتطبيق مستقل في قائمة تطبيقات أودو
    'auto_install': False,
}

