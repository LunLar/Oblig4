from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route('/')
def Hjem():

    return render_template('index.html', active_page = 'Hjem')


@app.route('/om_meg')
def Om_meg():

    return render_template('om_meg.html', active_page = 'Om_meg')


@app.route('/python_flask')
def Python_Flask():

    return render_template('python_flask.html', active_page = 'Python_Flask')




if __name__ == '__main__':
    app.run(debug=True)