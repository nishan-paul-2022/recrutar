import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'done_backend_job_recruitment.settings')

application = get_asgi_application()
