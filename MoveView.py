import sublime, sublime_plugin

class MoveViewLeftCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.window()
		group, index = window.get_view_index(self.view)
		if 0 < index:
			window.set_view_index(self.view, group, index - 1) # Move left.

class MoveViewRightCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.window()
		group, index = window.get_view_index(self.view)
		numViews = len(window.views()) # Index goes from 0 to n - 1.
		maxIndex = numViews - 1
		if index < maxIndex:
			window.set_view_index(self.view, group, index + 1) # Move right.
