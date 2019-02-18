#/bin/bash
ps -A | grep python | awk 'BEGIN{system("CMD=`cat /proc/$1/cmdline` && echo $CMD && kill `$1` && `$CMD`")}'
#ps -A | grep python | awk 'BEGIN{system("CMD=`cat /proc/$1/cmdline | sed 's/\x0/ /g'` && kill `$1` && `$CMD`")}'
