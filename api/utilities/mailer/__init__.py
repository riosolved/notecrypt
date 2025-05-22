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

def context(
    provider,
    **kwargs
):
    try:
        match provider:
            case PROVIDERS.GOOGLE.APP_PASSWORD:
                # yield Google_AppPassword.mailer(**kwargs)
                pass
            case PROVIDERS.BREVO:
                # yield Brevo.mailer(**kwargs)
                pass
            case _:
                ValueError(f"Unknown mailer: {provider}")
    finally:
        if hasattr(mailer, "close"):
            mailer.close()
