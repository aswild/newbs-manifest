#! /usr/bin/env python

import os

def main(project_list, manifest_projects=None, **kwargs):
    print("Hello world from post-sync.py!")
    print("Current directory is %s"%os.getcwd())
