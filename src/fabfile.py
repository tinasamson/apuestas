from fabric.api import env
from fabric.api import run, prefix
from fabric.context_managers import cd
#from fabric.operations import sudo


def test():
    env.host = [""]
    env.user = []
