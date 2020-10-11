#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
        from django.core.management.utils import get_random_secret_key

        remote_base_name = os.path.dirname(os.path.abspath(__file__))
        remote_path_name = os.path.normpath(os.path.join(remote_base_name, 'mysite/local_settings.py'))

        secret_key = get_random_secret_key()
        text = 'SECRET_KEY = \'{0}\''.format(secret_key)

        with open(remote_path_name, mode='w') as f:
            f.write(text)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
