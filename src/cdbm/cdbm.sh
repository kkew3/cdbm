cdbm() {
    local fun=
    local q=
    while getopts ":hlcen:" arg "$@"; do
        case $arg in
            h)
                fun=help
                ;;
            l)
                fun=list-bm
                ;;
            c)
                fun=list-ct
                ;;
            e)
                fun=edit-bm
                ;;
            n)
                fun=append-cwd
                q="$OPTARG"
                ;;
            +n)
                fun=prepend-cwd
                q="$OPTARG"
                ;;
            ?)
                echo "ERROR: unknown option '$OPTARG'" >&2
                return 1
                ;;
            :)
                echo "ERROR: missing argument in option '$OPTARG'" >&2
                return 1
                ;;
        esac
        shift
    done
    if [ -z $fun ]; then
        fun=query
        q="$*"
    fi

    local ret_path=
    case $fun in
        query)
            ret_path="$(command cdbm query "$q")"
            if [ -n "$ret_path" ]; then
                [ "$CDBM_ECHO" = "1" ] && echo "$ret_path"
                cd "$ret_path"
            fi
            ;;
        append-cwd|prepend-cwd)
            command cdbm $fun "$q"
            ;;
        *)
            command cdbm $fun
            ;;
    esac
}
