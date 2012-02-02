My .vimrc Configuration
01-20-2012    

VIM is my favorite text editor. It's powerful, customizable, and available on all platforms (default on unix-systems, gvim/macvim on pc/osx-systems). Most importantly, it's extremely efficient once you learn the movements and power commands. My hands rarely have to leave the keyboard when editing.

The .vimrc is the configuration file. I consider my .vimrc pretty basic and a good starting point for beginners to VIM. I would also suggest to understand every setting before adding to your .vimrc file. Here are a few of my favorite settings:

1. Remap : to ;
nnoremap ; :
The nnoremap setting remaps : to ; in normal mode and thus, saves a key stroke (shift + ;) when entering command mode. It seems trivial, but when a file is saved a 100 times in a day, it adds up.

2. Remap <esc> to jj
inoremap jj
Similar to the setting above, this setting remaps the often-used <esc> key to jj key press combo. It's pretty rare for code or text to contain the letters "jj" in succession. Now, a simple jj tap will bring VIM out of insert mode.

3. Map <leader> to ,
let mapleader = ","
The <leader> key is your own personal modifier key and is default as \. This setting allows for easier usage of <leader> macros.

4. Map NERDTree toggle to ,n.
nnoremap <leader>n :NERDTreeToggle
This allows me to map the <leader> key in conjunction with n to quickly toggle NERDTree. NERDTree is a VIM plugin used to navigate and control the files in a workspace easier.

All in all, my favorite .vimrc settings increase the comfort of using the editor. I've found them extremely useful and hope they can be the same for you.
