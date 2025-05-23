from ._anvil_designer import PayersTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ...Layouts.LayoutComponents.Payer_Information import Payer_Information
from ...utils.Navigation import navigate

class Payers(PayersTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    # Any code you write here will run before the form opens.

  def aetna_button_click(self, **event_args):
    navigate('default_payer_information')

  def get_payer_information_data(self):
    return self.item['text_box']
