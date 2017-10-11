#!/bin/sh
echo "Check for debug lines"

FILES_PATTERN='\.(py)(\..+)?$'
FORBIDDEN='pdb.set_trace()'
git diff --cached --name-only | \
grep -E $FILES_PATTERN | \
GREP_COLOR='4;5;37;41' xargs grep --color --with-filename -n $FORBIDDEN && echo "COMMIT REJECTED Found '$FORBIDDEN' references. Please remove them before commiting" && exit 1
echo "run Jenkins or tests"
/home/venv/bin/python ./manage.py test
RESULT=$?
[ $RESULT -ne 0 ] && echo "COMMIT REJECTED Found Failed Test Cases. Please fix them before commiting" && exit 1
exit 0
