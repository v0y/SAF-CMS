from fabric.api import cd, env, execute, prefix, run, shell_env, task


env.project_name = None
env.project_root = None
env.settings_module = None
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

    env.settings_module = {
        'lolwtf.pl': 'safcms.settings.settings_lolwtf_pl'
    }[name]


@task
def pyc():
    """
    Remove *.pyc files
    """
    run('find . -name "*.pyc" -delete')


@task
def deploy(branch='master'):
    """
    Make deploy
    """
    assert env.project_root, PROJECT_NOT_SET_ERROR_MSG
    assert env.venv_path, PROJECT_NOT_SET_ERROR_MSG
    assert env.settings_module, PROJECT_NOT_SET_ERROR_MSG

    with cd(env.project_root), \
            prefix('source %s' % env.venv_path), \
            shell_env(DJANGO_SETTINGS_MODULE=env.settings_module):

        execute(pyc)
        run('pip install -r requirements.txt')
        run('git reset --hard')
        run('git pull --force origin %s' % branch)
        run('git submodule init')
        run('git submodule update --force')
        run('./manage.py syncdb --noinput')
        run('./manage.py collectstatic --noinput')
        execute(restart)


@task
def restart():
    assert env.project_name, PROJECT_NOT_SET_ERROR_MSG

    run('sudo service uwsgi restart %s' % env.project_name)
