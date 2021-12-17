#!/bin/bash
if [ ! -d "vimwiki" ]; then
    git clone https://github.com/apsid/vimwiki
fi
vim -c ':VimwikiIndex'
