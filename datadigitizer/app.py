import os
from flask import Flask, jsonify, render_template, json, request

app = Flask(__name__)

def setup_app():
    configure_app()

def configure_app():
    '''Configure app loading in order from:
    '''
    here = os.path.dirname(os.path.abspath( __file__ ))
    # parent directory
    config_path = os.path.join(os.path.dirname(here), 'app.cfg')
    if os.path.exists(config_path):
        app.config.from_pyfile(config_path)
    ADMINS = app.config.get('ADMINS', '')
    if not app.debug and ADMINS:
        import logging
        from logging.handlers import SMTPHandler
        mail_handler = SMTPHandler('127.0.0.1',
                                   'server-error@no-reply.com',
                                   ADMINS, 'annotator error')
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

@app.route("/")
def home():
    return render_template('index.html', task_id=1)

@app.route('/transcribe/<task_id>')
def transcribe(task_id):
    key = 'tSZWuSYlRmdV7JpMI4E8oMQ'
    db = OurDatabase(key)
    task = db.get_task(task_id)[0]
    return render_template('transcribe.html', task=task)


class OurDatabase(object):
    def __init__(self, key):
        import gdata.spreadsheet.text_db
        username = app.config['GDOCS_USERNAME']
        password = app.config['GDOCS_PASSWORD']
        self.client = gdata.spreadsheet.text_db.DatabaseClient(
                username=username,
                password=password
                )
        dbs = self.client.GetDatabases(key)
        if not dbs:
            raise Exception('DB not found')
        self.db = dbs[0]
        tables = self.db.GetTables(name='task')
        self.task_table = tables[0]
    
    def all_tasks(self):
        records = self.task_table.GetRecords(1, 20)
        return records

    def get_task(self, task_id):
        rec = self.task_table.FindRecords('id==%s' % task_id)
        return rec


if __name__ == "__main__":
    setup_app()
    app.run(host='0.0.0.0', debug=True)
