#!/usr/bin/env python
#Imcber was here
#commit1
#commit2
#commit3
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ximbo.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
