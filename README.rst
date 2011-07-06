Crowd source data digitizing.

Install
=======

Instructions for a developer install (you may want to the following in a
virtualenv)::

  # install pip (or easy_install)
  # install requirements
  pip install -r requirements
  pip install -e .

Now you can run the app::

  python datadigitizer/app.py

Visit: http://localhost:5000/

Technical
=========

We use google docs as backend database. This makes it incredibly easy to add
and edit tasks as you can just edit them in google spreadsheet.

For develepers documentation on the API and python code for this can be found here:

  * Source file (with docs): http://code.google.com/p/gdata-python-client/source/browse/src/gdata/spreadsheet/text_db.py
  * Using Google Spreadsheets as a Database in the Cloud: http://www.youtube.com/watch?v=rWCLROPKug0


