# Dommert's Flask Foundation
# Dommert@Gmail.com (GitHub.com/Dommert)

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world(title='Hello World'):
    return render_template('foundation/default.html', title=title)

@app.route('/about')
def about(title='About Page'):
    return render_template('foundation/onecol.html', title=title)

    @app.route('/<path:path>')
def catch_all(title='Catch All' , content='Catch All URL'):
        return render_template('foundation/onecol.html', title=title)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
