#!/bin/bash
# This basj=h script shows the allowed methods of an http serer
curl -sI "$1" | grep 'Allow' | awk '{$1 = ""; sub(/^ /, ""); print $0}'
