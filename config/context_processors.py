from .models import MainConfig


def main_settings(request):
    main_config = MainConfig.get_solo()
    return {
        "main_config": main_config,
    }
