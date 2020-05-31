#!/bin/bash

options=("qtile" "Brave Browser" "Quit")
PS3="Install software: "

if [ "$EUID" -ne 0 ] 
    then echo "Installing software without root? Seriously?"
    exit
fi

select opt in "${options[@]}";
do
    case $opt in
        "qtile")
            echo "Installing qtile"
            pip3 -v 2>/dev/null || apt-get install python3-pip -y
            pip3 install xcffib
            pip3 install --no-cache-dir cairocffi
            apt-get install libpangocairo-1.0-0 -y
            git clone git://github.com/qtile/qtile.git ~/tmp/qtile
            pip3 install ~/tmp/qtile/
            break
            ;;
        "Brave Browser")
            echo "Installing Brave Browser"
            curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
            echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
            apt update
            apt install brave-browser -y
            break
            ;;
        "Quit") 
            break
            ;;
        *) echo "Invalid option: $opt";;
    esac
done
