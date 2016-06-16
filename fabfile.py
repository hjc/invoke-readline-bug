from fabric.api import *

@task
def pdb_example():
    local("python pdb_test.py")

@task
def readline_example():
    local("python")
