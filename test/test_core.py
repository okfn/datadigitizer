from flask import json, url_for

from datadigitizer.app import app, setup_app, OurDatabase

def setup():
  setup_app()

class TestItAll(object):
    def setup(self):
        self.app = app.test_client()
        key = 'tSZWuSYlRmdV7JpMI4E8oMQ'
        self.db = OurDatabase(key)

    def test_get_tasks(self):
        out = self.db.all_tasks()
        assert len(out)
        print out[0].content
        assert out[0].content['spreadsheetid'] == 'tDMCil7PxwW7DQeBHlckl9A'

    def test_get_task(self):
        out = self.db.get_task('1')
        assert out[0].content['spreadsheetid'] == 'tDMCil7PxwW7DQeBHlckl9A'

