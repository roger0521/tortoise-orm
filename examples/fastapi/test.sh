#!/bin/bash

#ABSPATH=`readlink -f $0`
#DIRPATH=`dirname $ABSPATH`
#cd ${DIRPATH}

####### Test #######

pytest -v tests/tests_user.py --capture=no

####################
