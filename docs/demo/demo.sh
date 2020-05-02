#!/usr/bin/env bash

. docs/demo/demo-magic.sh

echo -e "\e[35m# Hi, welcome to xsdata demo!"
pe "xsdata --help"
pe "clear"

cd ../xsdata-samples

pe "xsdata sabre/schemas --package sabre.models"
pe "ls -la sabre/models"
pe "bat sabre/models/bargain_finder_max_common_types_v1_9_7.py"

cd ../xsdata

echo -e "\e[35m# See help for more, bye bye :)"
sleep 2
