title: My .bash configuration
#url:
#template:
tags: config
#sitemap settings
#sm_f: weekly
#sm_p: 0.5

# My .bash config

I use [http://bash.org](bash), not for any particular reason, but because it was
the default with OS X(osx).  I've only customised it slightly (for the same
reasons as my minimal vim(vim) configuration, because I use many servers that
aren't my own, so I need to rely on defaults more often than not).

```

alias ls="ls -F -G"
alias love=/Applications/love.app/Contents/MacOS/love

export ANDROID_HOME=/opt/android-sdk/
export ANDROID_NDK=/opt/android-ndk/

export PATH="/opt/android-sdk/platform-tools:/opt/android-ndk:/opt/apache-ant/bin:$PATH"

# full path in title
export PROMPT_COMMAND='echo -ne "\033]0;$PWD\007"'
# fill path in prompt (makes copy-pasta URLs for SCP easier)
export PS1='\[$(tput setaf 6 ; tput setab 0 )\]\u@\h:\w \$\[$(tput sgr0)\] '

alias vim="/Applications/MacVim.app/Contents/MacOS/Vim"
alias waste='/Users/Local/waste/waste.py'

complete -d cd
. ~/bin/z.sh
```

The only plugin I really include is [https://github.com/TODO/z](z), which uses
fuzzy logic to 'guess' which directory I am trying to move to.  

You can see the rest of my computing environment on config(config).
