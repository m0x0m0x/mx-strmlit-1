#!/usr/bin/env bash
set -euo pipefail

##################################
# Initial setup ffor the project
##################################

# Colors
RE='\e[0;31m'
GR='\e[0;32m'
BL='\e[0;34m'
YL='\e[0;33m'
NC='\e[0m'

# Commands
b1() {
    clear
    echo -e "${YL}------------------------------------------------"
    echo -e "Installing required libraries for running this streamlit application"
    echo -e "------------------------------------------------${NC}"
}

i1() {
    echo -e "Install the following"
    echo -e "${RE}1. streamlit${NC}"
    echo -e "${RE}2. pandas${NC}"
    echo -e "${RE}4. matplotlib${NC}"
    echo -e ""
    uv add \
        streamlit pandas matplotlib rich
    uv tree
    echo -e "${GR}Done-Begin BootyDance ${NC}"
}

# Exection Sequence
b1
i1
