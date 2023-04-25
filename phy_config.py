
# You can also put your plugins in ~/.phy/plugins/.

from phy import IPlugin

# Plugin example:
#
# class MyPlugin(IPlugin):
#     def attach_to_cli(self, cli):
#         # you can create phy subcommands here with click
#         pass

c = get_config()
c.Plugins.dirs = [r'C:\Users\<your-username>\.phy\plugins']
c.TemplateGUI.plugins = ['n_spikes_views', 'SplitShortISI', 'Recluster']  # list of plugin names to load in the TemplateGUI
