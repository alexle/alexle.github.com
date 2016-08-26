---
title: Keeping A Github Fork Updated
date: 08-12-2012
image:
meta: It's hard to remember all the Github commands. Here's how to keep your Gibhub Fork updated.
---

I still find myself having to look up how to update my forked Github repositories so I'm creating a quick post for future use. The steps below are what I use to keep the code I've forked current with its original repository.

##Setting up the Clone##

If you haven't cloned your forked repository yet, do so with:

<pre><code class=python>git clone git@github.com:alexle/bootstrap.git</code></pre>

<pre><code class=python>cd bootstrap</code></pre>

In the commands above, "alexle" and "bootstrap" should be replaced with your Github name and the name of your fork, respectively.

##Configuring the Upstream##

Add another remote repository, one that points to the original repository. It can be any name you choose; I always name mine "upstream" to stay consistent.

<pre><code class=python>git remote add upstream git://github.com/twitter/bootstrap.git</code></pre>

Your remote repositories can be viewed with "git remote -v". Note there should already be an "origin" remote target in your fork.

##Updating the Fork##

To pull changes from the main repository into your forked repository:

<pre><code class=python>git fetch upstream</code></pre>

<pre><code class=python>git merge upstream/master</code></pre>

<pre><code class=python>git push</code></pre>

And voila! This brings your repo up-to-date.
