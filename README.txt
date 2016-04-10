Labor2Day

- when creating branches, in order to track the branch use this function:
	- git checkout -b <branch name> --track origin/<branch name>
	- for example, if the branch is beforeFlask, then use:
		git checkout -b beforeFlask --track origin/beforeFlask
	- in order to to see all remotes use: git branch -a