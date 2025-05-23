from ._anvil_designer import Payer_InformationTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from ....utils.Navigation import navigate

class Payer_Information(Payer_InformationTemplate):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print('p')
    print(self.parent)
    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    print('cLICKED')
    navigate('payer_information_2')

