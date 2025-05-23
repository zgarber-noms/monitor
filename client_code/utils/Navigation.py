import anvil.server
from anvil import open_form
from . import emitter

nav_dic = {
  'login': {
    'active': None,
    'form_name': 'Pages.Login' } ,
  'dashboard': {
    'active': 'dashboard',
    'form_name': 'Pages.Dashboard' } ,
  'customers': {
    'active': 'customers',
    'form_name': 'Pages.Customers' } ,
  'tickets': {
    'active': 'tickets',
    'form_name': 'Pages.Tickets.Tickets' } ,
  'new_ticket': {
    'active': 'tickets',
    'form_name': 'Pages.Tickets.NewTicket' } ,
  'ticket': {
    'active': 'tickets',
    'form_name': 'Pages.Tickets.Ticket' } ,
  'connections': {
    'active': 'connections',
    'form_name': 'Pages.Connections' } ,
  'jobs': {
    'active': 'jobs',
    'form_name': 'Pages.Jobs' } ,
  'arrival': {
    'active': 'arrival',
    'form_name': 'Pages.Arrival' } ,
  'monitor': {
    'active': 'monitor',
    'form_name': 'Pages.Monitor' } ,
  'home': {
    'active': 'home',
    'form_name': 'Pages.Home' } ,
  'payers': {
    'active': 'payers',
    'form_name': 'Pages.Payers' } ,

  'payer_information': {
    #'active': 'payer',
    'form_name': 'Layouts.LayoutComponents.Payer_Information' },
  'payer_information_2': {
    #'active': 'payer',
    'form_name': 'Layouts.LayoutComponents.Payer_Information_2' },
  
  'default_payer_information': {
    'active': 'default_payer_information',
    'form_name': 'Pages.DefaultPayerInformation' },

  'aetna_payer_information': {
    'active': 'aetna_payer_information',
    'form_name': 'Pages.AetnaPayerInformation' },

}
def navigate(page, **page_props):    
  open_form(nav_dic[page]['form_name'], **page_props)
  if nav_dic[page]['active']: 
    emitter.emit('set_active_nav_style', nav_name = nav_dic[page]['active'])
