function old_pwd --description 'Print the current working directory, NOT shortened to fit the prompt'
    if test "$PWD" != "$HOME"
        printf "%s" (echo $PWD|sed -e 's|/private||' -e "s|^$HOME|~|")
    else
        echo '~'
    end
end

function fish_prompt --description 'Write out the prompt'
	
    set_color 565656
    printf (date +%H:%M:%S)

    set_color white 

    printf " %s "  $USER

    set_color green

    printf (__fish_git_prompt)

    set_color yellow

    printf " %s" (old_pwd)

    set_color white

    printf "> "
end
