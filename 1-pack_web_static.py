#!/usr/bin/python3
"""Generating a .tgz file"""
from fabric.context_managers import lcd
from datetime import datetime
from fabric.operations import local


def do_pack():
    local("mkdir -p versions")

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f"web_static_{timestamp}.tgz"

    with lcd("web_static"):
        res = local(f"tar -czf ../versions/{filename} *", capture=True)

    if res.succeeded:
        return f"versions/{filename}"
    else:
        return None
if __name__ == "__main__":
    do_pack()
