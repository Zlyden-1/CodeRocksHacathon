from django.contrib import admin

from . import models

admin.site.register(models.User)
admin.site.register(models.Order)
admin.site.register(models.OrderStatus)
admin.site.register(models.Category)
admin.site.register(models.UserReview)
