#!/usr/bin/python3
"""Creates and distributes an archive to web servers"""
from datetime import datetime
import os.path
from fabric.api import local
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["100.26.250.243", "54.236.33.98"]


def do_pack():
    local("mkdir -p versions")
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_path = "versions/web_static_{}.tgz".format(timestamp)
    local("tar -cvzf {} web_static".format(archive_path))
    return archive_path


def do_deploy(archive_path):
    if not isfile(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_filename = os.path.basename(archive_path)
        archive_folder = ('/data/web_static/releases/' +
                          os.path.splitext(archive_filename)[0])
        sudo('mkdir -p {}'.format(archive_folder))
        sudo('tar -xzf /tmp/{} -C {}'.format(archive_filename, archive_folder))
        sudo('rm /tmp/{}'.format(archive_filename))
        sudo('rm /data/web_static/current')
        sudo('ln -s {} /data/web_static/current'.format(archive_folder))
        return True
    except Exception as e:
        print("Error deploying archive:", e)
        return False


def deploy():
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
