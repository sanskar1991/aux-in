# aux-in
A music player.

### Technology Stack

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [HTML](https://html.com/)
* CSS
* [JavaScript](https://www.javascript.com/)

### Installation in Windows

* Download and install [Python
  3.6.x](https://www.python.org/ftp/python/3.6.8/python-3.6.8.exe).  For this
  guide, we assume Python is installed in `C:\Python35`.
* Download the Pip (Python package installer) bootstrap script
  [get-pip.py](https://bootstrap.pypa.io/get-pip.py).
* In the command prompt, run `C:\Python35\python.exe get-pip.py` to install
  `pip`.
* In the command prompt, run `C:\Python35\scripts\pip install virtualenv` to
  install `virtualenv`.

### Installation in Ubuntu

Python 3 is preinstalled in Ubuntu. Virtualenv and pip necessarily aren't, so:

* `sudo apt-get install python-virtualenv python-pip`

### Creating and activating a virtualenv

Go to the project root directory and run:

Windows:

```
c:\location_of_project>c:\Python35\scripts\virtualenv --system-site-packages venv
c:\location_of_project>venv\Scripts\activate
```

Ubuntu:

```
virtualenv -p /usr/bin/python3 --system-site-packages venv
source venv/bin/activate
```

Starting the project
--------------------

After activating the virtualenv do the following

```
cd app
pip install -r requirements.txt
python manage.py runserver
```

Now it should be visible in the browser at
[`http://127.0.0.1:8000/`](http://127.0.0.1:8000/).
