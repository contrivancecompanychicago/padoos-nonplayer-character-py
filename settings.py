pip install --upgrade sentry-sdk

import sentry_sdk
from sentry_sdk.integrations.gcp import GcpIntegration

sentry_sdk.init(
    dsn="https://04ae81a005bf6452059fdde4097b30ff@o229048.ingest.us.sentry.io/4506903157080064",
    integrations=[GcpIntegration()],
)

def http_function_entrypoint(request):
    ...

sentry_sdk.init(
    dsn="https://04ae81a005bf6452059fdde4097b30ff@o229048.ingest.us.sentry.io/4506903157080064",
    integrations=[
        GcpIntegration(timeout_warning=True),
    ],
)
