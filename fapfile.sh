#!/bin/sh
HOST="qwerty"
REMOTE="rails/d_askra_pl"

setup() {
    cd $REMOTE
}

deploy() {
    git pull
    git submodule init
    git submodule update
    ./manage.py syncdb --noinput
    ./manage.py migrate
    ./manage.py collectstatic --noinput
    restart
}

managepy() {
    ./manage.py $@
}

restart() {
    touch tmp/restart.txt
}

update_python() {
    git pull
    restart
}
