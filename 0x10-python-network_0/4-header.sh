#!/bin/bash
# This script adds a header to the GET request sent
curl -sH "X-School-User-Id: 98" "$1"
