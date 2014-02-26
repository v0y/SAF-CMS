homepage
========

My homepage xD

Notes
-----

### Package installation

```
PYTHONPATH=/home/mironczyk/rails/homepage/site-packages easy_install -d /home/mironczyk/rails/homepage/site-packages [package]==[version]
```

### Deploy

TODO: move to fapfile or something

```sh
$ cd rails/homepage
$ git pull
$ git submodule update
$ cd vendor/OSB-CSS
$ vim css/osb.less  # enable theme
$ lessc osb.less > osb.css
$ cd ../../
$ ./manage.py collectstatic
$ touch tmp/restart.txt
```
