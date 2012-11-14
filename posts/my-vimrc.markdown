My .Vimrc Configuration
01-20-2012    

[VIM][1] is my favorite text editor. It's powerful, customizable, and available on all platforms (default on unix-systems, gvim/macvim on pc/osx-systems). Most importantly, it allows me to get my work in an extremely **efficient** manner. Once you learn the movements and power commands, your hands rarely have to leave the keyboard when editing.

The .vimrc is the configuration file. I consider [my .vimrc][2] pretty basic and a good starting point for beginners to VIM. I would suggest to anyone editing their .vimrc to understand each setting before using them. Here are a few of my favorite settings:

####Remap Command Mode####
<div id="code">
<font color="#f0e68c"><b>nnoremap</b></font>&nbsp;;&nbsp;:<br>
</div>

The nnoremap setting remaps : to ; in normal mode and thus, saves a key stroke (shift + ;) when entering command mode. It seems trivial, but when a file is saved a 100 times in a day, it adds up.

####Remap &lt;esc&gt; to jj####
<div id="code">
<font color="#f0e68c"><b>inoremap</b></font>&nbsp;jj&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">esc</font><font color="#ffdead">&gt;</font><br>
</div>

Similar to the setting above, this setting remaps the often-used &lt;esc&gt; key to jj key press combo. It's pretty rare for code or text to contain the letters "jj" in succession. Now, a simple jj tap will bring VIM out of insert mode.

####Map &lt;leader&gt; key####
<div id="code">
<font color="#f0e68c"><b>let</b></font>&nbsp;mapleader&nbsp;<font color="#f0e68c"><b>=</b></font><font color="#ffa0a0">&quot;,&quot;</font><br>
</div>

The &lt;leader&gt; key is your own personal modifier key and is default as \. This setting allows for easier usage of <leader> macros.

####Map NERDTree toggle to &lt;leader&gt;####
<div id="code">
<font color="#f0e68c"><b>map</b></font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">leader</font><font color="#ffdead">&gt;</font>n&nbsp;:NERDTreeToggle<font color="#ffdead">&lt;</font><font color="#ffdead">CR</font><font color="#ffdead">&gt;</font><br>
</div>

This allows me to map the &lt;leader&gt; key in conjunction with n to quickly toggle [NERDTree][3]. NERDTree is a VIM plugin used to navigate and control the files in a workspace easier.

####Add Google Search to VIM command line####
<div id="code">
<font color="#87ceeb">&quot; key mapping for google search</font><br>
<font color="#f0e68c"><b>function</b></font>! Google<font color="#ffdead">()</font><br>
&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>call</b></font>&nbsp;<font color="#98fb98">inputsave</font><font color="#ffdead">()</font><br>
&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>let</b></font>&nbsp;searchterm&nbsp;<font color="#f0e68c"><b>=</b></font>&nbsp;<font color="#98fb98">input</font><font color="#ffdead">(</font><font color="#ffa0a0">'Google: '</font><font color="#ffdead">)</font><br>
&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>call</b></font>&nbsp;<font color="#98fb98">inputrestore</font><font color="#ffdead">()</font><br>
&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>return</b></font>&nbsp;searchterm<br>
<font color="#f0e68c"><b>endfunction</b></font><br>
<font color="#f0e68c"><b>map</b></font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">leader</font><font color="#ffdead">&gt;</font>g&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">ESC</font><font color="#ffdead">&gt;</font>:! /usr/bin/open -a &quot;/Applications/Google Chrome.app&quot; '<a href="https://google.com/search?q=">https://google.com/search?q=</a><font color="#ffdead">&lt;</font><font color="#ffdead">C-R</font><font color="#ffdead">&gt;</font>=Google()<font color="#ffdead">&lt;</font><font color="#ffdead">CR</font><font color="#ffdead">&gt;</font>'<font color="#ffdead">&lt;</font><font color="#ffdead">CR</font><font color="#ffdead">&gt;&lt;</font><font color="#ffdead">CR</font><font color="#ffdead">&gt;</font>
</div>

With this macro, typing <leader\>g brings up the prompt "Google:". Once a search string is entered, a web browser will open (or tab if one is already opened) with a Google search of the string. This is great for those moments when I want to quickly look something up without having to locate my web browswer.

####Toggle VIM Blog Mode####
<div id="code">
<font color="#87ceeb">&quot; macro for blog writing</font><br>
<font color="#f0e68c"><b>function</b></font>&nbsp;ToggleBlog<font color="#ffdead">()</font><br>
&nbsp;&nbsp;<font color="#f0e68c"><b>if</b></font>&nbsp;&amp;wrap<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>echo</b></font>&nbsp;<font color="#ffa0a0">&quot;Blog OFF&quot;</font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>setlocal</b></font>&nbsp;<font color="#cd5c5c">nowrap</font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>set</b></font>&nbsp;<font color="#cd5c5c">virtualedit</font>=all<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>setlocal</b></font>&nbsp;<font color="#cd5c5c">lines</font>=50&nbsp;<font color="#cd5c5c">columns</font>=200<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>color</b></font>&nbsp;desert&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>setlocal</b></font>&nbsp;<font color="#cd5c5c">guifont</font>=menlo<font color="#f0e68c"><b>:</b></font>h11<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>silent</b></font>!&nbsp;nunmap&nbsp;<font color="#f0e68c"><b>&lt;</b></font><font color="#f0e68c"><b>buffer</b></font><font color="#f0e68c"><b>&gt;</b></font>&nbsp;<font color="#f0e68c"><b>k</b></font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>silent</b></font>!&nbsp;nunmap&nbsp;<font color="#f0e68c"><b>&lt;</b></font><font color="#f0e68c"><b>buffer</b></font><font color="#f0e68c"><b>&gt;</b></font>&nbsp;<font color="#f0e68c"><b>j</b></font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>silent</b></font>!&nbsp;nunmap&nbsp;<font color="#f0e68c"><b>&lt;</b></font><font color="#f0e68c"><b>buffer</b></font><font color="#f0e68c"><b>&gt;</b></font>&nbsp;<font color="#ffa0a0">0</font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>silent</b></font>!&nbsp;nunmap&nbsp;<font color="#f0e68c"><b>&lt;</b></font><font color="#f0e68c"><b>buffer</b></font><font color="#f0e68c"><b>&gt;</b></font>&nbsp;$<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>silent</b></font>!&nbsp;iunmap&nbsp;<font color="#f0e68c"><b>&lt;</b></font><font color="#f0e68c"><b>buffer</b></font><font color="#f0e68c"><b>&gt;</b></font>&nbsp;<font color="#f0e68c"><b>k</b></font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>silent</b></font>!&nbsp;iunmap&nbsp;<font color="#f0e68c"><b>&lt;</b></font><font color="#f0e68c"><b>buffer</b></font><font color="#f0e68c"><b>&gt;</b></font>&nbsp;<font color="#f0e68c"><b>j</b></font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>silent</b></font>!&nbsp;iunmap&nbsp;<font color="#f0e68c"><b>&lt;</b></font><font color="#f0e68c"><b>buffer</b></font><font color="#f0e68c"><b>&gt;</b></font>&nbsp;<font color="#ffa0a0">0</font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>silent</b></font>!&nbsp;iunmap&nbsp;<font color="#f0e68c"><b>&lt;</b></font><font color="#f0e68c"><b>buffer</b></font><font color="#f0e68c"><b>&gt;</b></font>&nbsp;$<br>
&nbsp;&nbsp;<font color="#f0e68c"><b>else</b></font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>echo</b></font>&nbsp;<font color="#ffa0a0">&quot;Blog ON&quot;</font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>setlocal</b></font>&nbsp;<font color="#cd5c5c">wrap</font>&nbsp;<font color="#cd5c5c">linebreak</font>&nbsp;<font color="#cd5c5c">nolist</font><br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>set</b></font>&nbsp;<font color="#cd5c5c">virtualedit</font>=<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>setlocal</b></font>&nbsp;<font color="#cd5c5c">display</font>+=lastline<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>setlocal</b></font>&nbsp;<font color="#cd5c5c">lines</font>=50&nbsp;<font color="#cd5c5c">columns</font>=90<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>color</b></font>&nbsp;morning&nbsp;<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>setlocal</b></font>&nbsp;<font color="#cd5c5c">guifont</font>=menlo<font color="#f0e68c"><b>:</b></font>h14<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>noremap</b></font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">buffer</font><font color="#ffdead">&gt;</font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">silent</font><font color="#ffdead">&gt;</font>&nbsp;k&nbsp;gk<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>noremap</b></font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">buffer</font><font color="#ffdead">&gt;</font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">silent</font><font color="#ffdead">&gt;</font>&nbsp;j&nbsp;gj<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>noremap</b></font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">buffer</font><font color="#ffdead">&gt;</font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">silent</font><font color="#ffdead">&gt;</font>&nbsp;0&nbsp;g0<br>
&nbsp;&nbsp;&nbsp;&nbsp;<font color="#f0e68c"><b>noremap</b></font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">buffer</font><font color="#ffdead">&gt;</font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">silent</font><font color="#ffdead">&gt;</font>&nbsp;$&nbsp;g$<br>
&nbsp;&nbsp;<font color="#f0e68c"><b>endif</b></font><br>
<font color="#f0e68c"><b>endfunction</b></font><br>
<font color="#f0e68c"><b>noremap</b></font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">silent</font><font color="#ffdead">&gt;</font>&nbsp;<font color="#ffdead">&lt;</font><font color="#ffdead">leader</font><font color="#ffdead">&gt;</font>b&nbsp;:call ToggleBlog()<font color="#ffdead">&lt;</font><font color="#ffdead">CR</font><font color="#ffdead">&gt;</font><br>
</font>
</div>

Finally, this last macro allows me to toggle between my coding sessions and my writing sessions. When writing, I prefer a lighter colorscheme (color morning) and smaller width window for readability (columns=90). I also set my text to wrap (setlocal wrap) so my text doesn't run off the window. Since wrap is enabled, the movement keys don't work as efficiently, so the gk, gj, g0, g$ allows the cursor to move similarly to before.

All in all, my favorite .vimrc settings increase the comfort of using the editor and add a little fun utility for the lazy side in me. I've found them extremely useful and hope they can be the same for you.

[1]: http://en.wikipedia.org/wiki/Vim_(text_editor)
[2]: https://github.com/alexle/vimrc/blob/master/.vimrc
[3]: http://www.vim.org/scripts/script.php?script_id=1658
