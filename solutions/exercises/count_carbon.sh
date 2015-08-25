
for file in $*
    do
        echo -n $file": "
        grep ' C ' $file | wc -l
    done
    echo -n "Total: "
    grep ' C ' $* | wc -l
