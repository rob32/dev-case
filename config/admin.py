from django.contrib import admin

from solo.admin import SingletonModelAdmin

from config.models import MainConfig, SocialAccountsConfig

admin.site.register(MainConfig, SingletonModelAdmin)
admin.site.register(SocialAccountsConfig, SingletonModelAdmin)
