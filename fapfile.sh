#!/bin/sh
HOST="qwerty"
REMOTE="rails/d_askra_pl"

setup() {
    cd $REMOTE
}

restart() {
    touch tmp/restart.txt 
}

update_python() {
    git pull
    restart
}
