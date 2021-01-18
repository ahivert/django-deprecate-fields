from django.db import models
from django_deprecate_fields.deprecate_field import deprecate_field


class AbstractModel(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        abstract = True


class ModelWithDeprecatedField(AbstractModel):
    is_active = deprecate_field(models.BooleanField())


class ModelWithDeprecatedFieldCustomReturnValue(AbstractModel):
    is_active = deprecate_field(models.BooleanField(), True)


class ModelWithDeprecatedFieldCustomCallableReturnValue(AbstractModel):
    is_active = deprecate_field(models.BooleanField(), lambda: True)
