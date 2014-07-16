#!/usr/bin/env python2

from __future__ import print_function
from salt_kwargs_cmd import kwargs_spec
from voluptuous import Schema, Rename

@kwargs_spec('zypper', 'install',
             Schema({
                 'plus_repo': str,
                 Rename('without_cd', rename_to='--no-cd', default=True): bool
             }))
def install(name, **kwargs):
    print("Name:", name)
    print("cmd:", cmd)
    print("Final command:", cmd, name)
    print("kwargs:", kwargs)
    print()


install('vim')
install('vim', without_cd=False, plus_repo='http://example.com')
install('vim', without_cd='ololo')
install('vim', plus_repo=True)