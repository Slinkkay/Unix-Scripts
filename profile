
#Marks functions for navigating around the command line
export MARKPATH=$HOME/.marks 
function jump {  
    cd -P "$MARKPATH/$1" 2>/dev/null || echo "No such mark: $1" 
} 
function mark {  
    mkdir -p "$MARKPATH"; ln -s "$(pwd)" "$MARKPATH/$1" 
} 
function unmark {  
    rm -i "$MARKPATH/$1" 
} 
function marks { 
    ls -l "$MARKPATH" | sed 's/  / /g' | cut -d' ' -f9- | sed 's/ -/ -/g' && echo 
} 
 
# Git completion for display the git branch in the prompt
# Source a git completion script
if [ -f $HOME/scripts/git-completion.sh ]; then
       . $HOME/scripts/git-completion.sh
else
  echo "Could not find git completion script"
fi
 
# Sample Prompt using the git completion script
#export PS1='[\u@\h \W$(__git_ps1 " (%s)")]\$ '
