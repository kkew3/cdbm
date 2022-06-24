# `cdbm`

`cdbm` is a small shell script (and a few python scripts) that bookmarks directories one wishes to go to quickly.

```
cdbm -e
```

edit the bookmark file located at `~/.config/cdbm/cdbm`.
The format each line is `<bookmark_name><space><directory>`.
The `<bookmark_name>` must not contain any whitespace characters or `#` character.
The `<directory>` entry is allowed to contain whitespace characters `<space>` and `<tab>` and `#` character.

```
cdbm -l
```

list current bookmarks in `~/.config/cdbm/cdbm` and color the bookmark names in red.


```
cdbm [<query>]
```

enter the [`fzf`](https://github.com/junegunn/fzf) interactive interface and select the bookmarked directory to go to.


## Installation

`source /path/to/cdbm.sh` in your `.bashrc` or `.zshrc`.

## Vim ftplugin

[cdbm.vim](cdbm.vim) contains syntax highlighting definition of `~/.config/cdbm/cdbm`.
To install `cdbm.vim`, if using [`vim-plug`](https://github.com/junegunn/vim-plug), put the following to `~/.vimrc`:

```vim
Plug 'kkew3/cdbm.vim'
```
