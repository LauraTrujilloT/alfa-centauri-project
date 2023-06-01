# OhMyZSH Installation

>>> [YT Video](https://youtu.be/9eJ0HHHNuls)

1. Install Oh My Zsh: 
`sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"`

1. Install Powerlevel10k Theme
`git clone https://github.com/romkatv/powerlevel10k $ZSH_CUSTOM/themes/powerlevel10`

1. Install Auto Suggestions Plugin 
`git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions`

1. Install Syntax Highlighting
`git clone https://github.com/zsh-users/zsh-synt... $ZSH_CUSTOM/plugins/zsh-syntax-highlighting`

1. Open your .zshrc file with VIM
`vim ~/.zshrc` 

1. Set theme to (includes the quotes)
"powerlevel10k/powerlevel10k"

1. Activate Enable Correction
`#ENABLE_CORRECTION="true"`
to this
`ENABLE_CORRECTION="true"`

1. Add our plugins
`plugins=(git zsh-autosuggestions zsh-syntax-highlighting)`

1.  Save by pressing CNTRL + Q and then type Y to save

2.  Download [Nerd Fonts](https://www.nerdfonts.com)
