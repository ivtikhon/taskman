#!/bin/bash
BASEDIR="$(dirname $0)"
cd "${BASEDIR}"
python3 "${BASEDIR}/startserver.py" > /dev/null 2>&1 &
