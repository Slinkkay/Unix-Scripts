function jump 
    cd "$MARKPATH/$argv"
end
function mark 
    mkdir -p "$MARKPATH" 
    ln -s "$PWD" "$MARKPATH/$argv" 
end
function unmark 
    rm -i "$MARKPATH/$argv" 
end 
function marks 
    ls -l "$MARKPATH" | sed 's/  / /g' | cut -d' ' -f9- | sed 's/ -/ -/g' 
    echo
end

set -x MARKPATH $HOME/.marks