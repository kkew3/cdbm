cdbm() {
    local fun=
    local q=
    case "$1" in
        -h)
            fun=help
            ;;
        -l)
            fun=list-bm
            ;;
        -c)
            fun=list-ct
            ;;
        -e)
            fun=edit-bm
            ;;
        *)
            fun=query
            q="$*"
            ;;
    esac

    local ret_path=
    case $fun in
        query)
            ret_path="$(command cdbm query "$q")"
            if [ -n "$ret_path" ]; then
                [ "$CDBM_ECHO" = "1" ] && echo "$ret_path"
                cd "$ret_path"
            fi
            ;;
        *)
            command cdbm $fun
            ;;
    esac
}
