---
title: Hammerspoon Configuration
date: 2017-10-30
tags: [dotfiles]
published: true
layout: default
---
# Hammerspoon

[Hammerspoon](http://hammerspoon.org) is a OS X utility that provides a high
level of customisation to control the working environment. Using it, one can
specify configuration where events such as mouse clicks and drags, and keyboard
shortcuts can be used to trigger scripts or alter the environment as one
prefers.

### Caps Lock
For many, the caps lock key is one of the most useless keys on modern
keyboards; rarely used, it is one of the largest buttons on a keyboard with
little useful functionality.

On the other hand, the new Macbook Pros have eliminated the escape key, one of
the most important keys for a [vim](http://www.vim.org) user, replacing it with
the touch bar. While the escape "key" would still be present on the touch bar,
there is something reassuring about pressing a physical escape button.

An ideal solution to this is to replace the functionality of the caps lock key
with the escape key. Rather than trying to hit the missing escape key, it is
possible to map the escape key to the caps lock key, allowing for less hand
movement, as well as a experiencing the tactile feedback of an actual key,
rather than the touch bar.

Mapping the caps lock key to escape is fairly easy in OS X. Under System
Preferences, Keyboard, Modifier Keys, the option to use Escape key as the
action to perform when the caps lock key is pressed.

![OSX Keyboard Modifiers](/img/osx_keyboard_modifiers.png "OSX Keyboard Modifiers")

Hammerspoon and
[Karabiner-Elements](https://github.com/tekezo/Karabiner-Elements) take this to
a whole new level however, by allowing the caps lock key to function as an
escape key when pressed alone, **and** also acting as a "hyper" key when
pressed in conjunction with other keys. This "hyper" key opens up so many more
possibilities, for having global or application specific function keys,
especially when combined with Hammerspoon.


## Karabiner-Elements

The first element (pun intended) in this setup is the configuration for
Karabiner-Elements. The following code JSON should be saved in a file in
`~/.config/karabiner/karabiner.json`. This config remaps the caps lock key to
send the escape key when pressed alone, while sending the command, control and
option keys when pressed in conjunction with other keys.

```json
{
    "global": {
        "check_for_updates_on_startup": true,
        "show_in_menu_bar": true,
        "show_profile_name_in_menu_bar": false
    },
    "profiles": [
        {
            "complex_modifications": {
                "parameters": {
                    "basic.to_if_alone_timeout_milliseconds": 1000
                },
                "rules": [
                    {
                        "description": "Shift Capslock sends Shift-Hyper, or escape if by itself",
                        "manipulators": [
                            {
                                "from": {
                                    "key_code": "caps_lock",
                                    "modifiers": {
                                        "mandatory": [
                                            "left_shift"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "left_shift",
                                        "modifiers": [
                                            "left_command",
                                            "left_control",
                                            "left_option"
                                        ]
                                    }
                                ],
                                "to_if_alone": [
                                    {
                                        "key_code": "escape"
                                    }
                                ],
                                "type": "basic"
                            }
                        ]
                    },
                    {
                        "description": "Capslock sends Hyper, or escape if by itself",
                        "manipulators": [
                            {
                                "from": {
                                    "key_code": "caps_lock"
                                },
                                "to": [
                                    {
                                        "key_code": "left_command",
                                        "modifiers": [
                                            "left_control",
                                            "left_option"
                                        ]
                                    }
                                ],
                                "to_if_alone": [
                                    {
                                        "key_code": "escape"
                                    }
                                ],
                                "type": "basic"
                            }
                        ]
                    }
                ]
            },
            "devices": [],
            "fn_function_keys": [
                {
                    "from": {
                        "key_code": "f1"
                    },
                    "to": {
                        "consumer_key_code": "display_brightness_decrement"
                    }
                },
                {
                    "from": {
                        "key_code": "f2"
                    },
                    "to": {
                        "consumer_key_code": "display_brightness_increment"
                    }
                },
                {
                    "from": {
                        "key_code": "f3"
                    },
                    "to": {
                        "key_code": "mission_control"
                    }
                },
                {
                    "from": {
                        "key_code": "f4"
                    },
                    "to": {
                        "key_code": "launchpad"
                    }
                },
                {
                    "from": {
                        "key_code": "f5"
                    },
                    "to": {
                        "key_code": "illumination_decrement"
                    }
                },
                {
                    "from": {
                        "key_code": "f6"
                    },
                    "to": {
                        "key_code": "illumination_increment"
                    }
                },
                {
                    "from": {
                        "key_code": "f7"
                    },
                    "to": {
                        "consumer_key_code": "rewind"
                    }
                },
                {
                    "from": {
                        "key_code": "f8"
                    },
                    "to": {
                        "consumer_key_code": "play_or_pause"
                    }
                },
                {
                    "from": {
                        "key_code": "f9"
                    },
                    "to": {
                        "consumer_key_code": "fastforward"
                    }
                },
                {
                    "from": {
                        "key_code": "f10"
                    },
                    "to": {
                        "consumer_key_code": "mute"
                    }
                },
                {
                    "from": {
                        "key_code": "f11"
                    },
                    "to": {
                        "consumer_key_code": "volume_decrement"
                    }
                },
                {
                    "from": {
                        "key_code": "f12"
                    },
                    "to": {
                        "consumer_key_code": "volume_increment"
                    }
                }
            ],
            "name": "Default profile",
            "selected": true,
            "simple_modifications": [],
            "virtual_hid_keyboard": {
                "caps_lock_delay_milliseconds": 0,
                "keyboard_type": "ansi"
            }
        }
    ]
}
```


## Hammerspoon Configuration

The following Hammerspoon configuration should be saved to `~/.hammerspoon/init.lua`.

It defines `hyper` as the combination of command, control and option being
pressed at the same time, which has been remapped to the caps lock key.
`shyper` is defined as the same combination, in addition with the shift key.

There are various utility functions defined, then the main `hyper`/`shyper` key
bindings are specified.

For now, there are simple terminal, firefox and finder window launching, as
well as a quick shortcut for putting the computer's display to sleep.

Hammerspoon is not only limited to launching commands triggered by keystrokes.
There is a section devoted to window layout, sending windows to various grid
locations. If you imagine a screen being split into 4 quadrants, there are
various key bindings (in association with the caps lock/hyper remapping) to
send windows to occupy various quadrants. This allows a focused window to be
quickly mapped to a region of the screen.

There is also a section devoted to using the mouse to control layout of
windows. By grabbing the title bar of a window and dragging to either the edge
or corner of the screen, the related window will be resized and positioned
appropriately.

Concluding the configuration, there are a few miscellaneous items and comments
for future plans :)


```lua
--[ Defines ]-------------------------------------------------------------

hyper =  {"⌘", "⌥", "⌃"}	-- caps lock held down
shyper = {"⌘", "⌥", "⇧", "⌃"}	-- caps lock held down, with shift
hs.window.animationDuration = 0


--[ Functions ]---------------------------------------------------------
function findOrLaunch(a)
	local app = hs.application.find(a)
	if not app then
		hs.application.launchOrFocus(a)
	end
	return hs.application.find(a)
end

function fancyNotify(t,m)
     hs.notify.new({title=t, informativeText=m}):send():release()
end


--[ Bindings ]---------------------------------------------------------

-- hyper shortcuts
hs.fnutils.each({
	{ key = "a", func = function() 
      myTerm = findOrLaunch("iterm")
      myTerm:selectMenuItem({"Shell","New Window"}) 
      end
  },
  { key = "q", func = function()
      ffox = hs.appfinder.appFromName("Firefox")
      ffox:selectMenuItem({"File","New Window"})
      ffox:activate()
      end
  },
  { key = "z", func = function()
      finder = hs.appfinder.appFromName("Finder")
      finder:selectMenuItem({"File","New Finder Window"})
      finder:activate()
      end
  }
}, function(object) hs.hotkey.bind(hyper, object.key, object.func) end)

-- shyper shoutcuts
hs.fnutils.each({
  { key = "space", func = function()
      os.execute("pmset displaysleepnow")
      end 
  }
}, function(object) hs.hotkey.bind(shyper, object.key, object.func) end)



--[ grid ]---------------------------------------------------------------------
-- home made grid system works with hammerspoon's grid

hs.grid.setGrid('2x2')
hs.grid.setMargins('0x0')

function moveWindow(x, y, w, h)
	local win = hs.window.focusedWindow()
	local f = win:frame()
	local screen = win:screen()
	local max = screen:frame()

	f.x = max.x + (max.w*x)
	f.y = max.y + (max.h*y)
	f.w = max.w*w
	f.h = max.h*h
	win:setFrame(f)
end

-- bind hotkeys to grid 
hs.hotkey.bind(hyper,"y", function() moveWindow(0.0,0.0,0.5,0.5) end)
hs.hotkey.bind(hyper,"u", function() moveWindow(0.0,0.0,1.0,0.5) end)
hs.hotkey.bind(hyper,"i", function() moveWindow(0.5,0.0,0.5,0.5) end)
hs.hotkey.bind(hyper,"h", function() moveWindow(0.0,0.0,0.5,1.0) end)
hs.hotkey.bind(hyper,"j", function() moveWindow(0.0,0.0,1.0,1.0) end)
hs.hotkey.bind(hyper,"k", function() moveWindow(0.5,0.0,0.5,1.0) end)
hs.hotkey.bind(hyper,"n", function() moveWindow(0.0,0.5,0.5,0.5) end)
hs.hotkey.bind(hyper,"m", function() moveWindow(0.0,0.5,1.0,0.5) end)
hs.hotkey.bind(hyper,",", function() moveWindow(0.5,0.5,0.5,0.5) end)

--[ window dragging ]----------------------------------------------------------
dragging_window = nil
click_event = hs.eventtap.new({hs.eventtap.event.types.leftMouseDragged}, function(e)
	if dragging_window == nil  then
		-- check mouse is in titlebar
		local m = hs.mouse.getAbsolutePosition()
		local f = hs.window:focusedWindow():frame()
		local screen = hs.window:focusedWindow():screen()
		local max = screen:frame()
		if m.x > f.x and m.x < (f.x + f.w) then
			if m.y > f.y and m.y < (f.y + 21) then
				dragging_window = hs.window.focusedWindow()
				dragging_window_time = hs.timer.localTime()
			end
		end
	end
end)
unclick_event = hs.eventtap.new({hs.eventtap.event.types.leftMouseUp}, function(e)
	if dragging_window ~= nil then
		local m = hs.mouse.getAbsolutePosition()
		local f = hs.window:focusedWindow():frame()
		local screen = hs.window:focusedWindow():screen()
		local max = screen:frame()
		if m.x < 50 then
			if m.y < 200 then
				moveWindow(0.0,0.0,0.5,0.5)
			elseif m.y > (max.h-200) then
				moveWindow(0.0,0.5,0.5,0.5)
			else
				moveWindow(0.0,0.0,0.5,1.0)
			end
		elseif m.x > (max.w-50) then
			if m.y < 200 then
				moveWindow(0.5,0.0,0.5,0.5)
			elseif m.y > (max.h-200) then
				moveWindow(0.5,0.5,0.5,0.5)
			else
				moveWindow(0.5,0.0,0.5,1.0)
			end
		elseif m.y < 25 and m.x>200 and m.x < (max.w-200) then
				moveWindow(0.0,0.0,1.0,1.0)
		end
	end
	dragging_window = nil
end)
click_event:start()
unclick_event:start()


--[ hourly alarm ]----------------------------------------------------------
hs.timer.doAt("0:00","1h", function() hs.alert("Ding Dong") end)

--[ fan ]-------------------------------------------------------------------
--[[
	my mac has a very noisy fan, this just puts the CPU temperature and fan
	speeds in the title bar
]]--
local menu_bar = hs.menubar.new()
menu_bar:setTitle("¯\\_(ツ)_/¯")
hs.timer.doAt("0:00","1m", function() 
	local d = hs.execute("/Users/sduff/bin/osx-cpu-temp -f"):gsub("[\r\n]","")
	menu_bar:setTitle(d)
end)

--[ hazel-lite ]------------------------------------------------------------
--[[
	Hazel-lite file system cleanup and management
	
	Ideas
	- Downloads/Desktop
		- Tag files
		- _Actions
		- Delete old files, Archive files to monthly folders
		- Move dmg to Trash, then open them
		- Add mp3 files to iTunes (music directory)
		- Drop folder that automatically zips and files away
		- IFTTT download top photo from earthporn/unsplash to dropbox, and then sync dropbox to make wallpapers
		- monitor a folder for images, then create a shrunk version, then move them to website git directory, then add them to the git build. remove the exif info as well, add copyright, etc... Needs Exiftool (https://www.sno.phy.queensu.ca/~phil/exiftool/) or Imagemagick's mogrify (https://stackoverflow.com/questions/229446/how-do-i-add-exif-data-to-an-image)
		- Move Desktop files to Downloads
		- Delete files older than 1 week
		- Archive certain files to Evernote/Dropbox/etc...
		- Save to Evernote drop-folder
		- Move torrent files to VirtualMachine
		- Sync ebooks in dropbox
		- Regularly clear tmp folders
		- Regularly clear Outlook tempfiles (/private/var/folders/y3/g8b0sww1685gtyvx20c7ghpxrdx1c3/T/com.microsoft.Outlook) (maybe symlink ~/Outlook to this folder for future versions)
		- Delete files that were downloaded from localhost
		- Archive downloaded software (app, iso, dmg, deb, exe, pkg, rpm)
		- Move downloaded videos (mov, mp4, avi) to its own directory
		- Move epub,mobi,pdf to an ebooks directory, well named (use mdls to extract pdf metadata, or pdfminer, https://github.com/euske/pdfminer)
		- mdls - https://www.macissues.com/2014/05/12/how-to-look-up-file-metadata-in-os-x/
		- Weekly empty of Trash

	Resources
	- https://github.com/scottcs/dot_hammerspoon/blob/master/.hammerspoon/modules/hazel.lua
	- https://www.reddit.com/r/apple/comments/1wlxtr/do_you_use_hazel_what_are_some_of_your_coolest/

	- http://getawesomeness.herokuapp.com/get/osx	
	- http://awesomeawesome.party/awesome-macOS


	Other efficiency
  - https://msol.io/blog/tech/work-more-efficiently-on-your-mac-for-developers/
  - http://stevelosh.com/blog/2012/10/a-modern-space-cadet/ (The Grand daddy)

  Something about launch or cycle
  - https://github.com/szymonkaliski/Dotfiles/blob/b5a640336efc9fde1e8048c2894529427746076f/Dotfiles/hammerspoon/init.lua#L442-L485

--]]

--[ Huzzah - we're ready! ]----------------------------------------------------
fancyNotify("Hammertime","Captain Hammer!")
```

# Download

My configuration for Karabiner-Elements, Hammerspoon and other utilities can be downloaded from [my github config repository](https://github.com/sduff/dotfiles).

# References

* More [Hammerspoon sample configurations](https://github.com/Hammerspoon/hammerspoon/wiki/Sample-Configurations)
* [A Modern Space Cadet](http://stevelosh.com/blog/2012/10/a-modern-space-cadet/) An excellent writeup of one user's extensive custom configuration
