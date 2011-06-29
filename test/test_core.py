from flask import json, url_for

from datadigitizer.app import app, setup_app, OurDatabase

def setup():
  setup_app()

class TestItAll(object):
    def setup(self):
        self.app = app.test_client()

    def test_get_tasks(self):
        key = 'tSZWuSYlRmdV7JpMI4E8oMQ'
        db = OurDatabase(key)
        out = db.all_tasks()
        assert len(out)
        print out[0].content
        assert out[0].content['spreadsheetid'] == 'tDMCil7PxwW7DQeBHlckl9A'

