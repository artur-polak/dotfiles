# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal

# use windows key as mod
mod = "mod4"
# terminal = guess_terminal()

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(), desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(), desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(), desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(), desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(), desc="Switch window focus to other pane(s) of stack"),

    # Launch terminal
    Key([mod], "Return", lazy.spawn('termite'), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),

    #open prompt widget
    Key([mod], "r", lazy.spawncmd(),desc="Spawn a command using a prompt widget"),

    # Grow and shrink windows in MonadTall
    Key([mod], "h", lazy.layout.grow(), lazy.layout.increase_nmaster(), desc="Expand window"),
    Key([mod], "l", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), desc="Shrink window"),

    # Lauch Brave
    Key([mod], "b", lazy.spawn('brave-browser --restore-last-session'), desc="Brave Browser")
]

#groups = [Group(i) for i in ['main', 'media', 'dev', 'work', 'games']]

groups = [
    Group('main'),
    Group('media'),
    Group('dev'),
    Group('work'),
    Group('games', layout='max')
]


keys.extend([
    # mod1 + letter of group = switch to group
    Key([mod], 'a', lazy.group['main'].toscreen(), desc="Switch to group 'main'"),
    Key([mod], 's', lazy.group['media'].toscreen(), desc="Switch to group 'media'"),
    Key([mod], 'd', lazy.group['dev'].toscreen(), desc="Switch to group 'dev'"),
    Key([mod], 'f', lazy.group['work'].toscreen(), desc="Switch to group 'work'"),
    Key([mod], 'g', lazy.group['games'].toscreen(), desc="Switch to group 'games'"),
    # mod1 + shift + letter of group = switch to & move focused window to group
    Key([mod, "shift"], 'a', lazy.window.togroup('main', switch_group=True), desc="Switch to & move focused window to group 'main'"),
    Key([mod, "shift"], 's', lazy.window.togroup('media', switch_group=True), desc="Switch to & move focused window to group 'media'"),
    Key([mod, "shift"], 'd', lazy.window.togroup('dev', switch_group=True), desc="Switch to & move focused window to group 'dev'"),
    Key([mod, "shift"], 'f', lazy.window.togroup('work', switch_group=True), desc="Switch to & move focused window to group 'work'"),
    Key([mod, "shift"], 'g', lazy.window.togroup('games', switch_group=True), desc="Switch to & move focused window to group 'games'"),
    # # mod1 + shift + letter of group = move focused window to group
    Key([mod, "shift", "control"], 'a', lazy.window.togroup('main'), desc="Move focused window to group 'main'"),
    Key([mod, "shift", "control"], 's', lazy.window.togroup('media'), desc="Move focused window to group 'media'"),
    Key([mod, "shift", "control"], 'd', lazy.window.togroup('dev'), desc="Move focused window to group 'dev'"),
    Key([mod, "shift", "control"], 'f', lazy.window.togroup('work'), desc="Move focused window to group 'work'"),
    Key([mod, "shift", "control"], 'g', lazy.window.togroup('games'), desc="Move focused window to group 'games'"),
])

layouts = [
    #layout.Max(),
    #layout.Stack(num_stacks=2),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
     layout.MonadTall(
         border_width = 2,
         border_focus = "dd0000",
         border_normal = "1d2330"
         ),
     layout.Max()
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
colors = [["#282a36", "#282a36"], # panel background
          ["#434758", "#434758"], # background for current screen tab
          ["#ffffff", "#ffffff"], # font color for group names
          ["#ff5555", "#ff5555"], # border line color for current tab
          ["#8d62a9", "#8d62a9"], # border line color for other tab and odd widgets
          ["#668bd7", "#668bd7"], # color for the even widgets
          ["#e1acff", "#e1acff"]] # window name

widget_defaults = dict(
    font='sans',
#    font='Ubuntu Mono Nerd Font Complete Mono',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(
                    foreground = colors[2],
                    background = colors[0]
                    ),
                widget.GroupBox(
                    border_width = 3,
                    active = colors[2],
                    inactive = colors[2],
                    rounded = False,
                    highlight_color = colors[1],
                    highlight_method = 'line',
                    this_current_screen_border = colors[3],
                    this_screen_border = colors[4],
                    other_current_screen_border = colors[0],
                    other_screen_border = colors[0],
                    foreground = colors[2],
                    background = colors[0]
                    ),
                widget.Prompt(
                    #prompt=prompt,
                    foreground = colors[3],
                    background = colors[0]
                    ),
                widget.Sep(
                    linewidth = 0,
                    padding = 40,
                    foreground = colors[2],
                    backgrounnd = colors[0]
                    ),
                widget.WindowName(),
                widget.Systray(),
                widget.CPU(
                    format='{freq_current}GHz {load_percent}%', 
                    fmt='CPU: {}'
                    ),
                widget.Sep(
                    foreground = colors[2],
                    backgrounnd = colors[0]
                    ),
                widget.Memory(
                    format='{MemUsed} / {MemTotal} M', 
                    fmt='Mem: {}'
                    ),
                widget.Sep(),
                widget.DF(
                    visible_on_warn=False, 
                    format='{f} / {s} GB', 
                    fmt='Drive: {}'
                    ),
                widget.Sep(),
                widget.Net(
                    fmt='Net: {}'
                    ),
                widget.Sep(),
                widget.Clock(
                    format='%H:%M:%S %Y-%m-%d',
                    foreground = colors[2],
                    background = colors[5]
                    ),
                widget.Sep(),
                widget.Volume(),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
