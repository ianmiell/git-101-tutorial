from shutit_module import ShutItModule

class git_101_tutorial(ShutItModule):

	def build(self, shutit):
		shutit.send('cd /myproject')
		if shutit.send_and_get_output('git version') != 'git version 2.1.4':
			shutit.fail('unexpected git version')

		shutit.challenge(
			'''In this tutorial you will be asked to set up git on your machine,
create a repository, and add and commit some code to it.

You have a full bash shell, so can use vi, less, man etc..

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
				'reset_container_name':'imiell/git-101-tutorial:step_3',
				'ok_container_name':'imiell/git-101-tutorial:step_3'
			},
			num_stages=8
		)
		shutit.challenge('''Configure git to tell it who you are (user.name and user.email). Don't forget that CTRL-h will give you hints.''',
			'11',
			challenge_type='golf',
			expect_type='exact',
			hints=['man git config','git config --global'],
			congratulations='OK!',
			follow_on_context={
				'check_command':r"""cat -s <(git config -l | grep user.email | wc -l) <(git config -l | grep user.name | wc -l) | tr -d '\n'""",
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_3',
				'ok_container_name':'imiell/git-101-tutorial:step_4'
			}
		)
		shutit.challenge('''Initialize a git repo in the /myproject folder. Don't create a subfolder or give git a folder name.''',
			'cfcd208495d565ef66e7dff9f98764da',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[],
			congratulations='OK!',
			follow_on_context={
				'check_command':'cat <(git status -s)  <(git branch | wc -l)',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_4',
				'ok_container_name':'imiell/git-101-tutorial:step_5'
			}
		)
		shutit.challenge('''Create a file called 'mycode.py' and put the line:

#!/usr/bin/env python

in it.

Then run git status to see what git thinks is going on in this repo.''',
			'e2ac2db4ef94965e8f02095a27b65f2d',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['echo "#!/usr/bin/env python" > mycode.py'],
			congratulations='OK!',
			follow_on_context={
				'check_command':r'''cat <(sed 's/^[[:blank:]]*//;s/[[:blank:]]*$//' mycode.py | sed -e :a -e '/./,$!d;/^\n*$/{$d;N;};/\n$/ba') <(git status -s) <(find *)''',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_5',
				'ok_container_name':'imiell/git-101-tutorial:step_6'
			}
		)
		shutit.challenge('''Add this file to your git repo ready to commit.

Then try running 'git status' again to see how git's view of this file has
changed.''',
			'1a8779dd8b7a61f23de73bcc0702f920',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git add mycode.py'],
			congratulations='OK!',
			follow_on_context={
				'check_command':r'''cat <(sed 's/^[[:blank:]]*//;s/[[:blank:]]*$//' mycode.py | sed -e :a -e '/./,$!d;/^\n*$/{$d;N;};/\n$/ba') <(git status -s) <(find *)''',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_6',
				'ok_container_name':'imiell/git-101-tutorial:step_7'
			}
		)
		shutit.challenge('''Commit the file to the git repo.

Then run 'git log' to see the history of the repository has now started''',
			'912251e04d2205b833772a31ca95f330',
			challenge_type='golf',
			expect_type='md5sum',
			hints=['git commit'],
			congratulations='OK!',
			follow_on_context={
				'check_command':r'''cat <(sed 's/^[[:blank:]]*//;s/[[:blank:]]*$//' mycode.py | sed -e :a -e '/./,$!d;/^\n*$/{$d;N;};/\n$/ba') <(git status -s) <(find *)''',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_7',
				'ok_container_name':'imiell/git-101-tutorial:step_8'
			}
		)
		# TODO hints
		shutit.challenge('''Add the line 'import string' to the mycode.py file. Do not commit it. Do not add any empty lines.

Then run 'git status' and 'git log' to see the status of the file and the
change from git's point of view.''',
			'8b13003240e0f264617cfc0892e194d0',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[''],
			congratulations='OK!',
			follow_on_context={
				'check_command':r'''cat <(sed 's/^[[:blank:]]*//;s/[[:blank:]]*$//' mycode.py | sed -e :a -e '/./,$!d;/^\n*$/{$d;N;};/\n$/ba') <(git status -s) <(find *)''',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_8',
				'ok_container_name':'imiell/git-101-tutorial:step_9'
			}
		)
		shutit.challenge('''Add and commit the file again.

Again, you can run 'git status' and 'git log' to see what git thinks has happened.''',
			'814967123be30fe11960749d22564000',
			challenge_type='golf',
			expect_type='md5sum',
			hints=[''],
			congratulations='OK!',
			follow_on_context={
				'check_command':r'''cat <(sed 's/^[[:blank:]]*//;s/[[:blank:]]*$//' mycode.py | sed -e :a -e '/./,$!d;/^\n*$/{$d;N;};/\n$/ba') <(git status -s) <(find *)''',
				'context':'docker',
				'reset_container_name':'imiell/git-101-tutorial:step_9',
				'ok_container_name':'imiell/git-101-tutorial:step_10'
			}
		)
		return True


def module():
	return git_101_tutorial(
		'tk.shutit.git_101_tutorial', 1845506479.0001,
		description='',
		maintainer='',
		delivery_methods=['docker'],
		depends=['shutit.tk.setup']
	)
