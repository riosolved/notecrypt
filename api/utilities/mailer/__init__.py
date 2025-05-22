from contextlib import contextmanager
# from .google.app_password import Google_AppPassword
# from .brevo import Brevo
from .mailer import Mailer

PROVIDERS = {
    "GOOGLE": {
        "APP_PASSWORD": 'google_app-password'
    },
    "BREVO": 'brevo'
}

@contextmanager
def context(
    provider,
    **kwargs
):
    try:
        if provider == PROVIDERS['GOOGLE']['APP_PASSWORD']:
            pass
            # yield Google_AppPassword.mailer(**kwargs)
        elif provider == PROVIDERS['GOOGLE']['APP_PASSWORD']:
            pass
            # yield Brevo.mailer(**kwargs)
        else:
            ValueError(f"Unknown mailer: {provider}")
    finally:
        if hasattr(mailer, "close"):
            mailer.close()

__all__ = ["context", "PROVIDERS"]