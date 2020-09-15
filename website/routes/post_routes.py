import flask
import pathlib
import datetime
import json
from flask import url_for, redirect
from flask_mail import Message
from dotenv import dotenv_values
from website import app, mail


@app.route('/handle-contact-us-data', methods=['POST'])
def handle_contact_us_data():
    post_request = flask.request.form.to_dict()
    post_request.pop('button')
    contact_us_dir = pathlib.Path('./contact-us')
    contact_us_dir.mkdir(exist_ok=True)
    if any(post_request.values()):
        # This is `slightly` risky file naming because if the user makes another POST request
        # within one second of sending there previous one, there will be filenaming conflicts.
        # With the current implementation, the old file will just be overwritten,
        # mainly so that the data is consistent, as opposed to appending the data
        # to the existing file.
        post_data_loc = contact_us_dir / f"{format(datetime.datetime.today(), '%Y-%m-%d_%I.%M.%S.%p')}.json"
        with post_data_loc.open(mode='w') as file:
            json.dump(post_request, file, indent=4)

        # Send an email when someone fill outs the `Contact Us` form
        msg = Message(subject=f"{post_request['fname']} {post_request['lname']} filled out the Contact Us form!",
                      body=(f"First Name: {post_request['fname']}\n"
                            f"Last Name: {post_request['lname']}\n"
                            f"Reason for Contacting: {post_request['reason']}\n"
                            f"Email address: {post_request['eaddress']}"),
                      recipients=[dotenv_values()['contact_page_email']])
        mail.send(msg)

    return redirect(url_for('thanks_contact'))
