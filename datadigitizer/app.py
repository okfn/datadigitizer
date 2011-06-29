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
    return render_template('index.html')

@app.route('/transcribe')
def transcribe():
    return render_template('transcribe.html')


if __name__ == "__main__":
    setup_app()
    app.run(host='0.0.0.0', debug=True)
