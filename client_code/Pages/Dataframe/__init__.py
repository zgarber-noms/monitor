from ._anvil_designer import DataframeTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class Dataframe(DataframeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    df_md = anvil.server.call('df_markdown')
    self.rich_text_1.content = df_md
    
    # Any code you write here will run before the form opens.
