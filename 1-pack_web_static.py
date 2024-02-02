#!/usr/bin/python3
'''
Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
'''
from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    '''
        A .tgz compressor function with fab
    '''
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir('versions') is False:
            local('mkdir versions')
        filename = 'versions/web_static_{}.tgz'.format(date)
        local('tar -cvzf {} web_static'.format(filename))
        return filename
    except Exception:
        return None
