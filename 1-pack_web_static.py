#!/usr/bin/python3
"""Generating a .tgz file"""
from datetime import datetime
from fabric.api import local
import os
import subprocess


def do_pack():
    os.makedirs("versions", exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output = f"versions/web_static_{timestamp}.tgz"
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except subprocess.CalledProcessError as e:
        print(f"Error packing web_static: {e}")
        output = None
    except OSError as e:
        print(f"Error accessing file: {e}")
        output = None
    return output
if __name__ == "__main__":
    do_pack()
