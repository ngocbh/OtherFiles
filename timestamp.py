import datetime
import sublime, sublime_plugin
 
class TimestampCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    timestamp = " [%s]\t" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    self.view.insert(edit, self.view.sel()[0].begin(), timestamp)