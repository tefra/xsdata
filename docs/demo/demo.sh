#!/usr/bin/env bash

. docs/demo/demo-magic.sh

echo -e "\e[35m# Hi, welcome to xsdata demo!"
pe "xsdata generate --help"

sleep 1
clear

pe "xsdata tests/fixtures/primer/order.xsd --package tests.fixtures.primer"
pe "bat -n tests/fixtures/primer/__init__.py"
pe "bat -n tests/fixtures/primer/order.py"

ipython

echo -e "\e[35m# See help for more, bye bye :)"
sleep 1
