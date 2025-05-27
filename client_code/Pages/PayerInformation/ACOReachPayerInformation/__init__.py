from ._anvil_designer import ACOReachPayerInformationTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from ..RosterInformation import RosterInformation

class ACOReachPayerInformation(ACOReachPayerInformationTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.column_panel_1.add_component(RosterInformation())
    self.item['test_var'] = 'Test'
    self.refresh_data_bindings(())

    # Any code you write here will run before the form opens.
