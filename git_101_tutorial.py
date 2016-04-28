from shutit_module import ShutItModule

class git_101_tutorial(ShutItModule):

	def build(self, shutit):
		shutit.send('cd /myproject')
		shutit.challenge(
			'''In this tutorial you will be asked to set up git on your machine,
create a repository, and add and commit some code to it.

You have a full bash shell, so can use vi, less, man etc..

If any tools are missing or there are bugs raise a github request or contact
@ianmiell on twitter.

CTRL-] (right angle bracket) to continue.
''',
			'1',
			challenge_type='golf',
			expect_type='exact',
			hints=['Hit CTRL-]'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'echo 1',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_4',
				'ok_container_name':'imiell/git-101-tutorial:step_4'
			}
		)
		shutit.challenge('''Configure git to tell it who you are (user.name and user.email). Don't forget that CTRL-h will give you hints.''',
			'11',
			challenge_type='golf',
			expect_type='exact',
			hints=['man git config','git config --global','git config --global user.email "you@example.com"','git config --global user.name "Your Name"'],
			congratulations='OK!',
			follow_on_context={
				'check_command':r"""cat -s <(git config -l | grep user.email | wc -l) <(git config -l | grep user.name | wc -l) | tr -d '\n'""",
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_4',
				'ok_container_name':'imiell/git-101-tutorial:step_5'
			}
		)
		shutit.challenge('''Initialize a git repo in this folder. Don't create a subfolder or give git a folder name.''',
			'897316929176464ebc9ad085f31e7284',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git init'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat <(git status -s)  <(git branch | wc -l)',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_5',
				'ok_container_name':'imiell/git-101-tutorial:step_6'
			}
		)
		shutit.challenge('''Create a file called 'mycode.py' and put the line:

#!/usr/bin/env python

in it.

Then run git status to see what git thinks is going on in this repo.''',
			'e9babeb3800fad4d7f5ecf1c097b8be1',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['echo "#!/usr/bin/env python" > mycode.py'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat mycode.py <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_6',
				'ok_container_name':'imiell/git-101-tutorial:step_7'
			}
		)
		shutit.challenge('''Add this file to your git repo ready to commit.

Then try running 'git status' again to see how git's view of this file has
changed.''',
			'e62f504bd6c4bc37fe75de05111b0b7d',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git add mycode.py'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat mycode.py <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_7',
				'ok_container_name':'imiell/git-101-tutorial:step_8'
			}
		)
		shutit.challenge('''Commit the file to the git repo.

Then run 'git log' to see the history of the repository has now started''',
			'6f88182b0d012dbda84be60d202149be',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git commit'],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat mycode.py <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_8',
				'ok_container_name':'imiell/git-101-tutorial:step_9'
			}
		)
		# TODO hints
		shutit.challenge('''Add the line 'import string' to the mycode.py file. Do not commit it.

Then run 'git status' and 'git log' to see the status of the file and the
change from git's point of view.''',
			'd65ee5d18ffe6ece5a520155e06a24ad',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[''],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat mycode.py <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_9',
				'ok_container_name':'imiell/git-101-tutorial:step_10'
			}
		)
		shutit.challenge('''Add and commit the file again.

Again, you can run 'git status' and 'git log' to see what git thinks has happened.''',
			'a93424203ffcd103f1483b67e00dd1cc',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[''],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat mycode.py <(git status -s) <(find *)',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_10',
				'ok_container_name':'imiell/git-101-tutorial:step_11'
			}
		)
		shutit.pause_point('Tutorial complete! Feel free to mess around at the back :)')
		return True


def module():
	return git_101_tutorial(
		'tk.shutit.git_101_tutorial', 1845506479.0001,
		description='',
		maintainer='',
		delivery_methods=['docker'],
		depends=['shutit.tk.setup']
	)
