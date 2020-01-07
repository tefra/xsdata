#!/usr/bin/env bash

# terminalizer record demo -c config.yml

. demo-magic.sh

echo -e "\e[35m# Hi, welcome to xsdata demo!"
pe "xsdata --help"
pe "clear"

cd ../../../xsdata-samples

pe "xsdata xsd/sabre/BargainFinderMaxRQ_v1-9-7.xsd --package demo.sabre"
pe "ls -la demo/sabre"
pe "bat demo/sabre/bargain_finder_max_common_types_v1_9_7.py"

cd ../xsdata/docs/demo

echo -e "\e[35m# See help for more, bye bye :)"
sleep 2
# terminalizer render -o demo.gif demo
