Updating A Github Fork From The Original Repository
08-12-2012

I still find myself having to look up how to update my forked Github repositories so I'm creating a quick post for future use. The steps below are what I use to keep the code I've forked current with its main repository.

###Setting up the Clone###

If you haven't cloned your forked repository yet, do so with:

> git clone git@github.com:alexle/bootstrap.git

> cd bootstrap

In the commands above, "alexle" and "bootstrap" should be replaced with your Github name and the name of your forked repository, respectively.

###Configuring the Upstream###

Next, add another remote repository pointing to the original repository. It can be any name you choose; I always name mine "upstream" to stay consistent.

> git remote add upstream git://github.com/twitter/bootstrap.git

Your remote repositories can be viewed with "git remote -v". Note that there should already be an "origin" remote repository to your fork.

###Updating the Fork###

To pull the changes from the main repository into your forked repository:

> git fetch upstream

> git merge upstream/master

> git push

And voila! This brings your repo up-to-date.
