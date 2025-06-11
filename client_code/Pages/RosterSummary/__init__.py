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
    print('getting data...')
    # Any code you write here will run before the form opens.
    self.set_roster_summary_data()
    self.refresh_data_bindings()

  def set_roster_summary_data(self):
    
    roster_rme_results = anvil.server.call('get_payer_rme_most_recent_results')

    print(roster_rme_results.keys())
    print(roster_rme_results['ACO Reach']['Count'])

    print('---')

    LAST_RME_RUN_TEXT = 'Last RME Ran On: '
    LAST_RME_COUNT_TEXT = 'Last RME Load Patient Count: '
    LAST_RME_FILENAME_TEXT = 'Latest PROD-ODB File: '
    LAST_RME_COUNT_TEXT = '# of Patients: '
    
    self.item['ACO Reach Previous RME Count'] = LAST_RME_COUNT_TEXT + str(roster_rme_results['ACO Reach']['Count'])
    print(type(roster_rme_results['ACO Reach']['Date']))
    self.item['ACO Reach Previous RME Date'] = LAST_RME_RUN_TEXT + roster_rme_results['ACO Reach']['Date'].strftime("%Y-%m-%d")
    print('***')
    self.item['ACO Reach Previous RME Filename'] = str(NotImplemented) 



    
    self.item['Aetna Previous RME Count'] = roster_rme_results['Aetna']['Count']
    self.item['Aetna Previous RME Date'] = roster_rme_results['Aetna']['Date']

    self.item['Devoted Previous RME Count'] = roster_rme_results['Devoted']['Count']
    self.item['Devoted Previous RME Date'] = roster_rme_results['Devoted']['Date']

    '''
    self.item['MMOH Previous RME Count'] = roster_rme_results['MMOH']['Count']
    self.item['MMOH Previous RME Date'] = roster_rme_results['MMOH']['Date']

    self.item['Luminare Previous RME Count'] = roster_rme_results['Luminare']['Count']
    self.item['Luminare Previous RME Date'] = roster_rme_results['Luminare']['Date']

    self.item['Humana Previous RME Count'] = roster_rme_results['Humana']['Count']
    self.item['Humana Previous RME Date'] = roster_rme_results['Humana']['Date']

    self.item['Anthem MA Previous RME Count'] = roster_rme_results['Anthem MA']['Count']
    self.item['Anthem MA Previous RME Date'] = roster_rme_results['Anthem MA']['Date']

    self.item['Anthem Commercial Previous RME Count'] = roster_rme_results['Anthem Commercial']['Count']
    self.item['Anthem Commercial Previous RME Date'] = roster_rme_results['Anthem Commercial']['Date']
    '''
    print('done')
