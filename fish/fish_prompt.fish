function old_pwd --description 'Print the current working directory, NOT shortened to fit the prompt'
    if test "$PWD" != "$HOME"
        printf "%s" (echo $PWD|sed -e 's|/private||' -e "s|^$HOME|~|")
    else
        echo '~'
    end
end    

function fish_prompt --description 'Write out the prompt'
	
	set -l last_status $status

	if not set -q __fish_prompt_normal
		set -g __fish_prompt_normal (set_color normal)
	end

	set fish_color_git yellow
	set_color 565656
	printf (date "+%H:%M:%S ")

	# PWD
	set_color $fish_color_cwd
	echo -n (old_pwd)
	set_color $fish_color_git 

	printf '%s ' (__fish_git_prompt)

	if not test $last_status -eq 0
	set_color $fish_color_error
	end

	set_color normal
	echo -n '$ '

end
