from flask import Flask
from flask_mail import Mail
from flask import render_template

from flask_mail import Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'email@email.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_DEFAULT_SENDER'] = 'email@email.com'

mail = Mail(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send_mail')
def send_mail():
    try:
        msg = Message(
            'Message example',
            recipients=['email@email.com']
        )
        msg.body = 'message attachment test'
        msg.html = render_template('mail-template.html')
        with app.open_resource("./static/image.png") as fp:
            msg.attach("image.png", "image/png", fp.read())
        mail.send(msg)
    except Exception as e:
        print(e)
    return render_template("send_mail.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run()
