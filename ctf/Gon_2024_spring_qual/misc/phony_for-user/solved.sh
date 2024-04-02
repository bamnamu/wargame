#!/bin/bash
# solved.sh
find "$1" -iname "*.eml" -type f -exec echo -ne "FILE: {} --- " \; -exec check-dkim {} \;