" Vundle configuration
set nocompatible
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'gmarik/Vundle.vim'
"plugins

call vundle#end()
filetype plugin indent on


" set syntax highlighting if possible
if has("syntax")
  syntax on
endif

" Source a global configuration file if available
if filereadable("/etc/vim/vimrc.local")
  source /etc/vim/vimrc.local
endif

" mark column #80
highlight ColorColumn ctermbg=magenta
call matchadd('ColorColumn', '\%80v',100)

" change colorcheme
" colorscheme koehler
colorscheme badwolf

" mark tabs and spaces
exec "set listchars=tab:\uBB\uBB,trail:\uB7,nbsp:~"
set list

" map ; to :
noremap ; :

" add ruler at the end of line
set ruler

" do not beep on error
set visualbell

" show line numbers relative to current line
set relativenumber

" highlight line with cursor
set cursorline
set showcmd

" check indent config based on filename
filetype indent on
filetype plugin on

" allow autoindent, set tabs to 4 spaces
set autoindent
set shiftwidth=4
set softtabstop=4
set expandtab

" don't break line in the middle of the word
set linebreak

" code folding based on indent,max fold nesting, no folding on file open, and
" use space to fold/unfold
set foldmethod=indent
set foldnestmax=99
set nofoldenable
noremap <space> za

