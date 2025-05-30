import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ._anvil_designer import PrimaryTemplate


class Primary(PrimaryTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
