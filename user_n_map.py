from flask import Flask, session, request, render_template
import create_map

app = Flask(__name__)
app.secret_key = 'QWWCdmsgfjvsdoojetJNnaeejfncwkejnafnenanrQDWN'


@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Generate 'index.html' dynamically according to users input nicknames.
    """
    if request.method == 'POST':
        nickname = request.form['nick']
        if nickname and nickname not in session:
            session[nickname] = 'value'
        return render_template('index.html', twi_list=[i for i in session])
    session.clear()
    return render_template('index.html')


@app.route('/map', methods=['GET'])
def map():
    """
    Create Map with all inputed users of Twitter.
    """
    create_map.map_creator([i for i in session])
    session.clear()
    return render_template('Twi_map.html')


@app.errorhandler(404)
def problem():
    """
    Handle 404 error
    :return:
    """
    return render_template('Wrong.html'), 404


if __name__ == '__main__':
    app.run(debug=True)
