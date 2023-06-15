from django.db import models

class ActiveBaseEntityManager(models.Manager):
    use_in_migrations = True
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class DefaultEntityManager(models.Manager):
    use_in_migrations = True
    use_for_related_fields = True

    def get_queryset(self):
        return super().get_queryset()