#!/bin/bash
# Call this script with at least 3 parameters, for example
# sh scriptname 1 2 3
gnome-terminal --tab -e "sh Int.sh $1" --tab -e "sh Int2.sh"
