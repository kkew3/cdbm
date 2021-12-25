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
	local bmfile=~/.cdbm

	local ed="${EDITOR:-vim}"

	if [ "$1" = "-e" ]; then
		# edit the bookmark file
		"$ed" "$bmfile"
	elif [ "$1" = "-l" ]; then
		# print the bookmark file, while highlighting the bm names
		python3 -c "
import sys
for line in sys.stdin:
    tokens = line.split(maxsplit=1)
    sys.stdout.write('\\033[1;31m{}\\033[0m {}'.format(
        tokens[0], ''.join(tokens[1:])))
" < "$bmfile"
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
			echo "Bookmark file \"$bmfile\" is empty. Use \`cdbm e\` to add"
			echo "some bookmarks."
			return 2
		fi

		local selkey

		if [ -z "$1" ]; then
			selkey="$(cut -d' ' -f1 < "$bmfile" | fzf --no-multi)"
		else
			selkey="$(cut -d' ' -f1 < "$bmfile" | fzf --no-multi --query="$1")"
		fi
		if [ -z "$selkey" ]; then
			return 130
		fi

		local selpath="$(python3 -c "
import sys
for line in sys.stdin:
	tokens = line.rstrip('\\n').split(maxsplit=1)
	key = tokens[0]
	if key == '$selkey':
		print('' if len(tokens) <= 1 else tokens[1])
		break
" < "$bmfile")"
		if [ -z "$selpath" ]; then
			return 130
		fi

		printf "%s\n" "$selpath"
		cd "$selpath"
	fi
}
