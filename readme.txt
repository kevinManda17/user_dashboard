user_dashboard/
├── manage.py
├── Procfile
├── runtime.txt
├── .env
│
├── user_dashboard/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── accounts/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py               ← Sérialiseurs DRF (ProfileSerializer, GroupSerializer, etc.)
│   ├── views.py                     ← Vues Django classiques (TemplateView, CreateView, etc.)
│   ├── views_api.py                 ← Vues API REST Framework
│   ├── urls.py                      ← URLs pour les vues classiques
│   ├── urls_api.py                  ← URLs spécifiques à l’API REST
│   ├── tests.py
│   │
│   ├── templates/
│   │   └── accounts/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── profile_list.html
│   │       ├── profile_detail.html
│   │       ├── profile_form.html
│   │       ├── profile_confirm_delete.html
│   │       ├── group_list.html
│   │       ├── group_detail.html
│   │       └── group_form.html
│   │
│   └── static/
│       └── accounts/
│           ├── css/
│           │   └── custom.css
│           └── js/
│               └── main.js
│
├── theme/                   Application Tailwind CSS (gérée par django-tailwind)
│   ├── __init__.py
│   ├── apps.py
│   ├── static_src/
│   │   ├── src/
│   │   │   └── styles.css
│   │   ├── package.json
│   │   ├── postcss.config.js
│   │   └── tailwind.config.js
│   └── templates/
│       └── base.html
│
└── requirements.txt


│
├── frontend/   				Application React créée via create-react-app
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── components/
│       │   ├── Navbar.jsx
│       │   ├── ProfileList.jsx
│       │   ├── ProfileDetail.jsx
│       │   ├── GroupList.jsx
│       │   └── GroupDetail.jsx
│       ├── pages/
│       │   ├── LoginPage.jsx
│       │   ├── RegisterPage.jsx
│       │   ├── DashboardPage.jsx
│       │   └── NotFound.jsx
│       ├── index.js
│       └── styles/
│           └── index.css
