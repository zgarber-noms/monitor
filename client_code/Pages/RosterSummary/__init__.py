from ._anvil_designer import RosterSummaryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from ...Components.Icons.CheckMark import CheckMark
from ...Components.Icons.RedX import RedX
from ...Components.Icons.Hourglass import Hourglass


class RosterSummary(RosterSummaryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.ACOReach_Symbol_Container.add_component(Hourglass())
    self.MMOH_Symbol_Conatiner.add_component(Hourglass())
    self.AnthemCommercial_Symbol_Conatiner.add_component((Hourglass()))
    self.Devoted_Symbol_Conatiner.add_component(CheckMark())
    self.Aetna_Symbol_Container.add_component(CheckMark())
    # Any code you write here will run before the form opens.
