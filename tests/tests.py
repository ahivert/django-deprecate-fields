import logging
from django.test import TestCase
from django.core.management import call_command
from tests import models
import subprocess
from unittest import mock

class DeprecateFieldTests(TestCase):

    def test_deprecate_field_is_skipped_by_django(self):
        with self.assertRaises(TypeError) as e:
            models.ModelWithDeprecatedField(name="test", is_active=True)
        self.assertIn('is_active', str(e.exception))

    def test_deprecate_field_call_warning_on_write(self):
        _ = models.ModelWithDeprecatedField(name="test")
        with self.assertLogs(level=logging.WARNING):
            _.is_active = False

    def test_deprecate_field_default_return_value(self):
        instance = models.ModelWithDeprecatedField(name="test")
        self.assertIsNone(instance.is_active)

    def test_deprecate_field_custom_return_value(self):
        for model in (models.ModelWithDeprecatedFieldCustomCallableReturnValue, models.ModelWithDeprecatedFieldCustomReturnValue):
            with self.subTest(model):
                instance = models.ModelWithDeprecatedFieldCustomReturnValue(name="test")
                self.assertEqual(instance.is_active, True)

class ManagementCommandTest(TestCase):

    # @mock.patch("django_deprecate_fields.deprecate_field.sys.argv", return_value="makemigrations")
    def test_makemigrations_generate_nullable(self):
        call_command("makemigrations")


