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
    
    df_col, df_dict = anvil.server.call('get_df_to_datagrid')
    self.datagrid = DataGrid(columns=df_col)
    self.datagrid.items = df_dict
    self.column_panel_1.add_component(self.datagrid)

    
    # Any code you write here will run before the form opens.
