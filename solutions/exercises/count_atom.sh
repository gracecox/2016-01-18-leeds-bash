
for file in ${*:2}
    do
        echo -n $file": "
        grep " $1 " $file | wc -l
    done
    echo -n "Total: "
    grep " $1 " ${*:2}  | wc -l
