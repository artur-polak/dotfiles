" All system-wide defaults are set in $VIMRUNTIME/debian.vim and sourced by
" the call to :runtime you can find below.  If you wish to change any of those
" settings, you should do it in this file (/etc/vim/vimrc), since debian.vim
" will be overwritten everytime an upgrade of the vim packages is performed.
" It is recommended to make changes after sourcing debian.vim since it alters
" the value of the 'compatible' option.

" This line should not be removed as it ensures that various options are
" properly set to work with the Vim-related packages available in Debian.
runtime! debian.vim

" Uncomment the next line to make Vim more Vi-compatible
" NOTE: debian.vim sets 'nocompatible'.  Setting 'compatible' changes numerous
" options, so any other options should be set AFTER setting 'compatible'.
"set compatible

" Vim5 and later versions support syntax highlighting. Uncommenting the next
" line enables syntax highlighting by default.
if has("syntax")
  syntax on
endif

" If using a dark background within the editing area and syntax highlighting
" turn on this option as well
"set background=dark

" Uncomment the following to have Vim jump to the last position when
" reopening a file
"if has("autocmd")
"  au BufReadPost * if line("'\"") > 1 && line("'\"") <= line("$") | exe "normal! g'\"" | endif
"endif

" Uncomment the following to have Vim load indentation rules and plugins
" according to the detected filetype.
"if has("autocmd")
"  filetype plugin indent on
"endif

" The following are commented out as they cause vim to behave a lot
" differently from regular Vi. They are highly recommended though.
"set showcmd		" Show (partial) command in status line.
"set showmatch		" Show matching brackets.
"set ignorecase		" Do case insensitive matching
"set smartcase		" Do smart case matching
"set incsearch		" Incremental search
"set autowrite		" Automatically save before commands like :next and :make
"set hidden		" Hide buffers when they are abandoned
"set mouse=a		" Enable mouse usage (all modes)

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

" code folding based on indent,max fold nesting and no folding on file open
set foldmethod=indent
set foldnestmax=10
set nofoldenable

"
