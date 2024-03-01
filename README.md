# cdbm -- cd bookmark

## Introduction

`cdbm` is a Python-based utility that bookmarks directories one wishes to `cd` quickly.

## Usage


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

```
cdbm -f
```

print stats of visisted directories in descending order.


## Installation

1. Clone this project to `/path/to/repo`.
2. Under `/path/to/repo/` in terminal, run `BINDIR=/path/to/bin ./install.sh`, where `/path/to/bin` is where you'd like the `cdbm` executable to sit. Here, `/path/to/bin` must be an existing directory in `PATH`.
3. At the end of your bashrc or zshrc, write `eval "$(cdbm init)"`.
4. Reopen your shell to activate the configuration.

## Dependencies

OS: No plan to support Windows currently, but WSL could be (not tested) acceptable.

Python: need to have `python3` in `PATH`, with Python>=3.7.

Other binaries: [`fzf`](https://github.com/junegunn/fzf) is required.

## Environment variables

This environment variables can be exported to change the behavior of `cdbm`:

- `CDBM_RECORD_COUNT`: set to `1` to enable recording directory counts (see below).

## Files and directories

`~/.config/cdbm` directory will be created if not exists.
This directory will be used to hold:

- `~/.config/cdbm/cdbm`: The bookmark file, which defines all bookmarked directories. You may freely edit yourself.
- `~/.config/cdbm/count`: A json file containing how many times you've used `cdbm` on each bookmarked directory.

## Companion Vim ftplugin

[cdbm.vim](cdbm.vim) contains syntax highlighting definition of `~/.config/cdbm/cdbm`.
To install `cdbm.vim`, if using [`vim-plug`](https://github.com/junegunn/vim-plug), put the following to `~/.vimrc`:

```vim
Plug 'kkew3/cdbm.vim'
```

## Similar projects

Until recently, I find that the idea of bookmarking directories was first sourced from [mokemokechicken's post](https://qiita.com/mokemokechicken/items/69af0db3e2cd27c1c467), which was then extended by [mollifier's cd-bookmark](https://github.com/mollifier/cd-bookmark).
