from ._anvil_designer import ConnectionsTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...utils import Data 

class Connections(ConnectionsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    table = self.table_name_input.text
    schema = self.schema_name_input.text
    print(f'Table text : {table} \n SCh')
    #x= Data.df_as_markdown(table, schema)
    if not table:
      table = 'Salesforce_tmp_Providers_with_term_dates'
    if not schema:
      schema = 'NOMSWorkSpace'
      print(f'Schema {schema} \nTable {table}')
    self.text_area_1.text = f'Showing Data from Caboodle Table [{schema}].[{table}]'  
    x= anvil.server.call("get_data_from_caboodle", table, schema)
    self.rich_text_1.content = x
