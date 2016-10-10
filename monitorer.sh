#/usr/bin/bash
CPUTEMP=`istats cpu temp | grep -o '[0-9]*\.[0-9]*'`
FANSPEED=`istats fan speed | grep -o '[0-9]*\.[0-9]*'`
TIMESTAMP=`date '+%d.%m.%Y,%X'`

OUTFILE=/Users/tschmelzer/cpu_monitoring/cpu.log

echo "${CPUTEMP};${FANSPEED};${TIMESTAMP}" >> $OUTFILE
