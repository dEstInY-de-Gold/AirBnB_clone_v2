#!/usr/bin/python3
'''
Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy.
'''
from fabric.api import put, run, env
from os.path import exists

env_hosts = ['54.161.235.10', '54.237.74.89']


def do_deploy(archive_path):
    '''
        Archive distribution to servers
    '''
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split('/')[-1]
        no_exists = filename.split('.')[0]
        path = '/data/web_static/releases/'
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_exists))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, no_exists))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_exists))
        run('rm -rf {}{}/web_static'.format(path, no_exists))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_exists))
        return True
    except Exception:
        return False
