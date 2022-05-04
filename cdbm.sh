#!/bin/bash
# also exposed to /bin/zsh
cdbm()
{
	# ensure required binaries exist
	for cmd in python3 cat fzf vim; do
		if ! command -v $cmd > /dev/null; then
			echo "$cmd is required" >&2
			return 1
		fi
	done


	# set the location of the bookmark file
	local bmfile=~/.config/cdbm/cdbm
	local freqfile=~/.config/cdbm/freq
	mkdir -p ~/.config/cdbm

	local ed="${EDITOR:-vim}"

	# reference: https://stackoverflow.com/a/54755784/7881370
	local cdbm_basedir="$(dirname "${BASH_SOURCE[0]:-${(%):-%x}}")"

	if [ "$1" = "-e" ]; then
		# edit the bookmark file
		"$ed" "$bmfile"
	elif [ "$1" = "-l" ]; then
		# print the bookmark file, while highlighting the bm names
		python3 "$cdbm_basedir/list_cdbm.py" "$bmfile"
	elif [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
		# show help
		cat << EOF
Use \`cdbm [<query>]\` to jump to bookmarked directory interactively; if
<query> is provided, jump to the bookmark matched <query>.
Use \`cdbm -e\` to edit the bookmark file.
Use \`cdbm -l\` to color list the bookmarks
Use \`cdbm -h\` or \`cdbm --help\` to show this message and exit.
EOF
	else
		if [ ! -s "$bmfile" ]; then
			echo "Bookmark file \"$bmfile\" is empty. Use \`cdbm -e\` to add"
			echo "some bookmarks."
			return 2
		fi

		local selkey="$(sed '/^#/d' "$bmfile" \
			| cut -d' ' -f1 \
			| fzf --no-multi --select-1 --query="$1")"
		if [ -z "$selkey" ]; then
			return 130
		fi

		local selpath="$(python3 "$cdbm_basedir/select_cdbm.py" "$bmfile" "$selkey" "$freqfile")"
		if [ -z "$selpath" ]; then
			return 4
		fi

		if [ "$selpath" != "$(pwd)" ]; then
			printf "%s\n" "$selpath"
			cd "$selpath"
		fi
	fi
}
