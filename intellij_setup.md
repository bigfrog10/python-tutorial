### Set up IntelliJ Projects
First, download Python plugin for IntelliJ. Go to Settings from File menu
(Widnows) or Preferences(Mac), then click Plugins on the left. Find the Python
plugin and install it.

Then when create new project, select Python on the left. This is very important,
otherwise you won't be able to get Python SDK option later.

Now go to Module Settings to set up modules. Set up project Python SDK first so
that all modules can reference project Python SDK.

Then setup the source folder in each module(marked as blue color).

### Test Coverage Setup

To set up test coverage, configure the following in preferences/settings
![coverage setup](intellij_coverage.png)


### GIT repository

IntelliJ has GIT functionalities built in. On windows, TortoiseGIT is a nice
GUI. Another tool for github is: https://desktop.github.com/.

Command line tool is for more experienced users.
