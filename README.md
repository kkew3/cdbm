# `cdbm`

`cdbm` is a small shell script that bookmarks directories one wishes to go to quickly.

```bash
cdbm -e
```

edit the bookmark file located at `~/.cdbm`.
The format each line is `<bookmark_name><space><directory>`.
The `<bookmark_name>` must not contain any whitespace characters.
The `<directory>` entry is allowed to contain whitespace characters `<space>` and `<tab>`.


```bash
cdbm
```

enter the [`fzf`](https://github.com/junegunn/fzf) interactive interface and select the bookmarked directory to go to.
