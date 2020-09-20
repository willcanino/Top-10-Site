import flask
from website import app

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/2020-hp')
def _2020_hp():
    return flask.render_template('2020-hp.html')

@app.route('/about')
def about():
    return flask.render_template('about-us.html')

@app.route('/artist-home')
def artist_home():
    return flask.render_template('artist-homepage.html')

@app.route('/categories')
def categories():
    return flask.render_template('categories.html')

@app.route('/contact')
def contact():
    return flask.render_template('contact-us.html')

@app.route('/login')
def login():
    return flask.render_template('login-page.html')

@app.route('/sign-up')
def signup():
    return flask.render_template('sign-up-page.html')

@app.route('/thank-you-for-contacting-us')
def thanks_contact():
    return flask.render_template('thanks-for-contacting.html')

#Top 10 Albums :
@app.route('/categories/music/album/coutry/t10-country-ablum.html')
def country_album():
    return flask.render_template('categories/music/album/country/t10-country-ablum.html')

@app.route('/categories/music/album/edm/t10-edm-ablum.html')
def country_album():
    return flask.render_template('categories/music/album/edm/t10-edm-ablum.html')

@app.route('/categories/music/album/jazz/t10-jazz-ablum.html')
def country_album():
    return flask.render_template('categories/music/album/jazz/t10-jazz-ablum.html')

@app.route('/categories/music/album/pop/t10-pop-ablum.html')
def country_album():
    return flask.render_template('categories/music/album/pop/t10-pop-ablum.html')

@app.route('/categories/music/album/rap/t10-rap-ablum.html')
def country_album():
    return flask.render_template('categories/music/album/rap/t10-rap-ablum.html')

@app.route('/categories/music/album/rock/t10-country-ablum.html')
def country_album():
    return flask.render_template('categories/music/album/rock/t10-country-ablum.html')
