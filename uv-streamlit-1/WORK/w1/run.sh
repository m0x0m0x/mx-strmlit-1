#!/usr/bin/env bash
set -euo pipefail

##################################
# Commands for running the streamlit application
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
    echo -e "Running the application"
    echo -e "------------------------------------------------${NC}"
}

i1() {
    echo -e "Following Command being run"
    echo -e "${RE}uvx streamlit run panty.py${NC}"
    echo -e ""
    uvx streamlit run panty.py
}

# Exection Sequence
b1
i1
