---
layout: post
title: "Keeping A Github Fork Updated"
date: 2012-08-02
tags: programming
---

I still find myself having to look up how to update my forked Github repositories so I'm creating a quick post for future use. The steps below are what I use to keep the code I've forked current with its original repository.

## Setting up the Clone ##

If you haven't cloned your forked repository yet, do so with:

``` python
git clone git@github.com:alexle/bootstrap.git

cd bootstrap
```

In the commands above, "alexle" and "bootstrap" should be replaced with your Github name and the name of your fork, respectively.

## Configuring the Upstream ##

Add another remote repository, one that points to the original repository. It can be any name you choose; I always name mine "upstream" to stay consistent.

``` python
git remote add upstream git://github.com/twitter/bootstrap.git
```

Your remote repositories can be viewed with "git remote -v". Note there should already be an "origin" remote target in your fork.

## Updating the Fork ##

To pull changes from the main repository into your forked repository:

``` python
git fetch upstream

git merge upstream/master

git push
```

And voila! This brings your repo up-to-date.
