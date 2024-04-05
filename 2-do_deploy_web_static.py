#!/usr/bin/python3
""" distributes an archive to your web servers"""
from fabric.api import env, put, run, sudo
import os.path


env.hosts = ['100.26.250.243', '54.236.33.98']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    if not os.path.isfile(archive_path):
        return False
    try:
        put(archive_path, '/tmp/', use_sudo=True, password='betty')
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
