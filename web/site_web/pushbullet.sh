#!/bin/bash

API="o.03JEUTkj2Hl2i0Lj2nAM2jODfQkryUIk"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="Alert" -d body="$MSG"