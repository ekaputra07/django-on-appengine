django-on-appengine
===================

Testing pure Django app on Google Appengine + Cloud SQL.

Run on localhost
----------------

1. Make sure you've downloaded Google Appengine Python SDK (https://cloud.google.com/appengine/downloads)
2. Edit `activate` file, and change the GAE path to your GAE SDK path.
3. Make sure you have MySQL server installed and also have MySQL-python installed on your Python Path.
4. Setup the dev environment, run `source activate` or `. activate`.
5. Rename `settings-sample.py` to `settings.py` in `blogengine` folder, and edit as needed.
6. Run Syncdb, `python manage.py syncdb`.
7. Run the server with `dev_appserver.py .` (notice the dot at the end of command), and open the browser at localhost:8080.

Deployment
----------

1. Create DB server instance on Google Cloud console, connect to it via mysql client and create new database.
2. Run syncdb on cloud SQL db, `SETTINGS_MODE="prod" python manage.py syncdb`, this will setup tabels in remote DB.
3. Run `python manage.py collectstatic`.
4. Deploy to Appengine, run `appcfg.py update`.
