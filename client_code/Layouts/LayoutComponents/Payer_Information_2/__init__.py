from ._anvil_designer import Payer_Information_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class Payer_Information_2(Payer_Information_2Template):
  def __init__(self, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    print('p')
    print(self.parent)
    # Any code you write here will run before the form opens.
