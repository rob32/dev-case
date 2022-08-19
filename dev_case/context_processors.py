from .settings import UMAMI_DATA_WEBSITE_ID, UMAMI_SCRIPT_URL, USE_UMAMI_ANALYTICS


def umami_analytics(request):
    return {
        "use_umami": USE_UMAMI_ANALYTICS,
        "umami_id": UMAMI_DATA_WEBSITE_ID,
        "umami_url": UMAMI_SCRIPT_URL,
    }
