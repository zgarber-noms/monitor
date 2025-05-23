from ._anvil_designer import AppBaseTemplate
import anvil.users
from ....utils.Navigation import navigate
from anvil import *
import anvil.server

class AppBase(AppBaseTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)
    
  def dashboard_link_click(self, **event_args):
    navigate(page='home')

  def tickets_link_click(self, **event_args):
    navigate(page='tickets')

  def customers_link_click(self, **event_args):
    navigate(page='customers')

  def new_ticket_button_click(self, **event_args):
    navigate(page='new_ticket')

  def signout_links_click(self, **event_args):
    anvil.users.logout()
    navigate(page='login')

  def form_show(self, **event_args):
    if anvil.users.get_user():
      self.user_email_label.text = anvil.users.get_user()['name'] or anvil.users.get_user()['email']

  def connections_Link_click(self, **event_args):
    pass

  def connections_link_click(self, **event_args):
    open_form("Pages.Connections")
    #navigate(page='connections')

  def monitor_link_1_click(self, **event_args):
    navigate("monitor")

  def jobs_link_click(self, **event_args):
    navigate("jobs")

  def nav_link_1_click(self, **event_args):
    
    navigate('default_payer_information')
  
