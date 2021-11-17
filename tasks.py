from invoke import task

@task

def start(ctx):
    ctx.run("python3 src/index.py")

def test(ctx):
    ctx.run("pytest src")
