#!/bin/sh
SERVERNAME='startserver.py'
ps -ef | grep -w "$SERVERNAME" | egrep -v grep | awk '{print $2}' | xargs kill