from invoke import task

@task
def readline_example(ctx):
    ctx.run("python", pty=True)

@task
def pdb_example(ctx):
    ctx.run("python pdb_test.py", pty=True)
