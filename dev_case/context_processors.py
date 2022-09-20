from dev_case import settings


def umami_analytics(request):
    return {
        "use_umami": settings.USE_UMAMI_ANALYTICS,
        "umami_id": settings.UMAMI_DATA_WEBSITE_ID,
        "umami_url": settings.UMAMI_SCRIPT_URL,
    }


def plausible_analytics(request):
    return {
        "use_plausible": settings.USE_PLAUSIBLE_ANALYTICS,
        "plausible_data_domain": settings.PLAUSIBLE_DATA_DOMAIN,
        "plausible_url": settings.PLAUSIBLE_SCRIPT_URL,
    }
