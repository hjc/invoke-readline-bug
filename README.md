# Invoke PDB Bug Example

This Repository intends to demonstrate a bug with the wonderful
[Invoke](https://github.com/pyinvoke/invoke) library where certain readline
commands are not properly mirrored to child tasks, causing some oddness.

How does this manifest? As a "delay". If a user has a readline context open in
a sub-process owned by Invoke, and they attempt to use more advanced line
editing capabilities, such as moving the cursor, home, end, delete by word,
etc., the results will not be shown right away. However, if the
user then issues another piece of input (such as typing a letter), then the
readline context will instantly update, show the "delayed" action, and the one
causing the "refresh".

This is shown best by video: 

[![asciicast](https://asciinema.org/a/enggvan6f8c1c14b76g9ztxh0.png)](https://asciinema.org/a/enggvan6f8c1c14b76g9ztxh0)

## Setup

Just install a virtualenv and the latest invoke and you're good to go:

```sh
$ virtualenv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

## Testing

Run either of the two commands, via invoke, to see the readline oddities.

`pdb_example` will run a Python file that simply has two print statements with
a `pdb.set_trace()` in between them. Every time PDB is used from a sub-process
called by Invoke, the readline oddities will happen (e.g., if your test runner
has a `--pdb` option to auto-launch PDB on failures, this won't be fun).

`readline_example` will simply open a Python shell, using invoke. This shell
will exhibit all of the readline oddities as expected.

Once you've done that, re-run the same commands using `fab`, which should handle
everything beautifully.
