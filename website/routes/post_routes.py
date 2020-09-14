import flask
import pathlib
import datetime
import json
from flask import url_for, redirect
from website import app

@app.route('/handle-contact-us-data', methods=['POST'])
def handle_contact_us_data():
    post_request = flask.request.form
    contact_us_dir = pathlib.Path('./contact-us')
    contact_us_dir.mkdir(exist_ok=True)
    unparsed = post_request.to_dict(flat=False)
    unparsed.pop('button')
    parsed = {key: val[0] if len(val) == 1 else val for key, val in unparsed.items()}
    if any(parsed.values()):
        # This is `slightly` risky file naming because if the user makes another POST request
        # within one second of sending there previous one, there will be filenaming conflicts.
        # With the current implementation, the old file will just be overwritten,
        # mainly so that the data is consistent, as opposed to appending the data
        # to the existing file.
        post_data_loc = contact_us_dir / f"{format(datetime.datetime.today(), '%Y-%m-%d_%I.%M.%S.%p')}.json"
        with post_data_loc.open(mode='w') as file:
            json.dump(parsed, file, indent=4)

    return redirect(url_for('thanks_contact'))
