#!/bin/bash
# Display body of GET request. the if statement isnt necessay but why not>
[ "$(curl -sI "$1" | awk 'NR==1{print $2}')" == "200" ] && curl -sL "$1"
