import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
from ._anvil_designer import OptionPrimaryOnRightTemplate

class OptionPrimaryOnRight(OptionPrimaryOnRightTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    form_container = self.side_form_1.dom_nodes['form-container']
    form_container.style.width = '50px'
    form_container.style.background = "none"
    form_container.style.position = "relative"
    form_container.style.zIndex = "1"
    form_container.style.borderRight = "1px solid var(--grey-025)"
    form_container.classList.remove('form-panel')

    self.primary_content_1.dom_nodes['primary-container'].style.backgroundColor = '#f8f8f8'
