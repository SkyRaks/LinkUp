"""
ASGI config for a_core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from whitenoise import WhiteNoise
from pathlib import Path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'a_core.settings')

django_asgi_app = get_asgi_application()

# Wrap Django ASGI app with WhiteNoise for media files
BASE_DIR = Path(__file__).resolve().parent.parent
django_asgi_app = WhiteNoise(django_asgi_app, root=str(BASE_DIR / "media"), prefix='media/')

from a_chat import routing

application = ProtocolTypeRouter({
    "http": django_asgi_app, # this is config for http connection

    "websocket": AllowedHostsOriginValidator( # this is config for websocket connection
        AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns)) # this is how to create websocket protocol
    ),

})
