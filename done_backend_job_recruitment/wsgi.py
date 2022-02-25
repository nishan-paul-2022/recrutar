import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'done_backend_job_recruitment.settings')

application = get_wsgi_application()
