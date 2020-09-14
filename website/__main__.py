try:
    from website import app
    app.run(debug=True)
except ModuleNotFoundError:
    import click
    click.echo(click.style('To avoid this error use ', fg='yellow')
                + click.style('python -m website', fg='yellow', bold=True))
    # raise keyword will raise whatever error is excepted above
    raise
