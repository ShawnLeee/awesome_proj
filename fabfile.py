from fabric.api import run
from fabric.api import local
def host_type():
    run('uname -s')

def hello():
    print("hel")


def prepare_deploy():
    local("git add .")
    local("git add -p && git commit")
    local("git push")
