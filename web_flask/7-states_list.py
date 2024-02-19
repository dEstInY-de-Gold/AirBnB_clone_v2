#!/usr/bin/python
'''
A script that starts a Flask web application
'''
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    '''
    display a HTML page: (inside the tag BODY)
    H1 tag: “States”
            UL tag: with the list of all State objects present in
            DBStorage sorted by name (A->Z) tip
            LI tag: description of one State: <state.id>: <B><state.name></B>
    '''
    state = storage.all('State')
    return render_templte('7-states_list.html', states = state)


@app.teardown_appcontext
def teardown(exc):
    '''
    a Call to the method storage.close()
    '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
