#!/bin/bash
set -x
[[ -z "$SHUTIT" ]] && SHUTIT="$1/shutit"
[[ ! -a "$SHUTIT" ]] || [[ -z "$SHUTIT" ]] && SHUTIT="$(which shutit)"
if [[ ! -a "$SHUTIT" ]]
then
    echo "Must have shutit on path, eg export PATH=$PATH:/path/to/shutit_dir"
    exit 1
fi
$SHUTIT build -d docker --exam -l debug -o out.$(date +%s).log "$@" 
if [[ $? != 0 ]]
then
    exit 1
fi
