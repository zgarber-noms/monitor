from ._anvil_designer import RosterSummaryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from ...Components.Icons.CheckMark import CheckMark
from ...Components.Icons.RedX import RedX



class RosterSummary(RosterSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.ACOReach_Symbol_Container.add_component(CheckMark())
    # Any code you write here will run before the form opens.
