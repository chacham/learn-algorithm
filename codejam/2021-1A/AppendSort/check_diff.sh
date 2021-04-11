while true; do
    python3 generator.py > test_generated
    res1=`cat test_generated| python3 solve.py`
    res2=`cat test_generated| python3 solve2.py`
    echo $res1
    echo $res2
    if [ "$res1" != "$res2" ]; then
        echo "Not Equal!"
        exit 0
    fi
done
