# 📝 Odoo To-Do Management Module

A lightweight, customized Odoo application built for **Odoo Community Edition** using **Python** and **XML**. This module serves as a practical project showcasing Odoo's architectural framework and its Object-Relational Mapping (ORM) layer to automatically generate and manage PostgreSQL database structures.

---

## ✨ Features
- **Task Creation:** Create new tasks with unique titles and comprehensive descriptions.
- **Deadline Tracking:** A dedicated date picker to monitor task execution deadlines.
- **Status Management:** Toggle completion states easily via native boolean checkboxes.
- **Fully Integrated UI:** Tailored views including structured **List/Tree Views**, interactive **Form Views**, and dynamic main menus.

---

## 🛠️ Technology Stack
- **Backend Logics:** Python (Odoo ORM Framework)
- **Frontend / UI Layouts:** XML Architecture
- **Database Engine:** PostgreSQL
- **Recommended OS:** Linux (Ubuntu / Zorin OS)

---

## 📂 Module Directory Structure
```text
todo_management/
├── __init__.py          # Initializes the Python package for Odoo
├── __manifest__.py      # App descriptor, dependencies, and metadata configuration
├── models/              # Contains data schemas and business logic (Python)
│   ├── __init__.py
│   └── todo_task.py     # Database model mapping fields (Char, Text, Boolean, Date)
└── views/               # Contains user interface definitions (XML)
    └── todo_task_view.xml
```

---

## 🚀 Installation & Setup

### 1. Clone the Module
Copy or clone this repository into your Odoo custom addons directory:
```bash
cd /path/to/your/odoo/custom_addons/
git clone https://github.com
```

### 2. Update the Apps List
1. Start your Odoo server and enable **Developer Mode** from the general settings panel.
2. Navigate to the **Apps** dashboard.
3. Click on **Update Apps List** in the top navigation bar to trigger a registry sync.

### 3. Activate the Module
Search for **"To-Do Management"** or **"إدارة المهام اليومية"** in the app store filter, then click the **Activate** button.

---

## 👨‍💻 Developer Profile
- **Name:** [Abdalwhab Abdallah ]
- **Role:** Python & Odoo Software Engineer
- **GitHub:** [http://www.github.com/Abdalwhab1]
- **LinkedIn:** [http://www.Linkedin.com/in/Abdodata101]
