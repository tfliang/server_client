#!/bin/bash


workdir=$(cd $(dirname $0); pwd)
echo $workdir
cd $workdir/server
export PYTHONPATH=${workdir}
uvicorn main:app --host 0.0.0.0 --port 9001 --reload