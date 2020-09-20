# I (@TurretAA12) was initially going to try and use `click` instead of argparse but it seems that
# my intended use case it not the situation for using `click`.  Click
# requires me to add decorators to functions to add them as command.
# My issue is that I would like to be able to access all the data from
# the given arguments at throughout the entire application instead of
# dividing access to these parameters throughout each function.
import argparse
import logging
import subprocess
import time
import click
import os

parser = argparse.ArgumentParser(description="Use this to configure how the website runs.")

parser.add_argument('-nt', '--not-testing', action='store_false', dest='testing',
                    help=("Toggle this to disable testing mode. "
                          "When testing mode is enabled all the other options below are NOT avaliable."))
parser.add_argument('-a', '--autodeploy', action='store_true',
                    help="Toggle this to automatically update the website whenever a new Github commit is made.")
parser.add_argument('-r', '--restart', action='store_true',
                    help="Toggle this to automatically restart the website if it crashes.")
parser.add_argument('-d', '--delay', type=float, default=5,
                    help="Use this to set the delay between each check for new files on Github in seconds. (default: %(default)s seconds)")

try:
    from website import app
except ModuleNotFoundError:
    import click
    click.echo(click.style('To avoid this error use ', fg='yellow')
                + click.style('python -m website', fg='yellow', bold=True))
    # raise keyword will raise whatever error is excepted above
    raise

args = parser.parse_args()

def check_for_new_commits(delay=args.delay):
    while start_website.poll() is None:
        git_pull = subprocess.Popen("git pull".split(), stdout=subprocess.PIPE, text=True)
        git_pull.wait()
        status = git_pull.stdout.read()
        yield status != "Already up to date.\n"
        time.sleep(delay)

if args.testing:
    app.run(debug=True)
else:
    logging.basicConfig(level=logging.DEBUG,
                        format=click.style("%(asctime)s [%(process)d] [%(levelname)s] %(message)s", fg='cyan'),
                        datefmt="[%Y-%m-%d %H:%M:%S %z]")
    start_website_command = f"gunicorn -w {os.cpu_count() * 2 + 1} website:app"
    start_website = subprocess.Popen(start_website_command.split(), )
    running = True
    try:
        while running:
            for new_commit in check_for_new_commits():
                if new_commit:
                    # Using SIGTERM aka Ctrl-C
                    # End website gracefully
                    start_website.terminate()
                    logging.info("New commit detected! Restarting website.")
                    start_website = subprocess.Popen(start_website_command.split())
            running = args.restart
    except KeyboardInterrupt:
        start_website.terminate()
    start_website.wait()
