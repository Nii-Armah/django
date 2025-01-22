from django.shortcuts import make_toast
from django.test import SimpleTestCase


class MakeToastTests(SimpleTestCase):
    """Tests for make_toast utility function."""
    def test_make_toast(self) -> None:
        self.assertEqual(make_toast(), "toast")
