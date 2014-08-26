from fabric.api import cd, env, execute, prefix, run, task


env.project_root = None
env.venv_path = None
env.user = 'deployer'
env.host_string = 'lolwtf.pl'

ALLOWED_PROJECTS_NAMES = ['lolwtf.pl']
INCORRECT_PROJECT_ERROR_MSG = \
    'Incorrect project "{given_name}". Allowed projects names are: {allowed}'
PROJECT_NOT_SET_ERROR_MSG = 'Set project first (run command "project")'


@task(alias='p')
def project(name):
    """
    Set project variables

    :param name: project name
    """
    assert name in ALLOWED_PROJECTS_NAMES, INCORRECT_PROJECT_ERROR_MSG \
        .format(given_name=name, allowed=ALLOWED_PROJECTS_NAMES)

    env.project_root = '/var/lib/uwsgi/%s/production/' % name
    env.venv_path = '/var/lib/virtualenv/%s/production/bin/activate' % name
    env.project_name = name


@task
def deploy(branch='master'):
    """
    Make deploy
    """
    assert env.project_root, PROJECT_NOT_SET_ERROR_MSG
    assert env.venv_path, PROJECT_NOT_SET_ERROR_MSG

    with cd(env.project_root), prefix('source %s' % env.venv_path):
        run('git pull')
        run('git submodule init')
        run('git submodule update')
        run('./manage.py syncdb --noinput')
        run('./manage.py migrate --noinput')
        run('./manage.py collectstatic -l --noinput')
        execute(restart)


@task
def restart():
    assert env.project_name, PROJECT_NOT_SET_ERROR_MSG

    run('sudo service uwsgi restart %s' % env.project_name)
