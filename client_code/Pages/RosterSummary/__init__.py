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
  '''
    self.Payers = {
      DEVOTED :'Devoted',
      CONTIGO : 'Contigo',
      LUMINARE : 'Luminare',
      MMOH : 'MMOH',
      HUMANA : 'Humana',
      CPC : 'CPC',
      AETNA : 'Aetna',
      ACO_REACH : 'ACO Reach',
      ANTHEM_MA : 'Anthem MA',
      ANTHEM_COMM : 'Anthem Commercial',
      OPTUM : 'Optum'
    }
    self.Rosters = {
      CONTIGO_ROSTER : 'Contigo Roster',
      DEVOTED_ROSTER : 'Devoted Roster',
      OPTUM_ROSTER : 'Optum Roster',
      AETNA_ROSTER : 'Aetna Roster',
      ANTHEM_MA_ROSTER : 'Anthem MA Roster',
      ANTHEM_COMMERCIAL_ROSTER : 'Anthem Commercial Roster',
      ACO_REACH_ROSTER : 'ACO Reach Roster',
      HUMANA_ROSTER : 'Humana Roster',
      MMOH_Roster : 'MMOH Roster',
      LUMINARE_ROSTER : 'Luminare Roster',
      CPC_ROSTER : 'CPC Roster'
    }
    '''
  def set_roster_summary_data(self):

    roster_rme_results = anvil.server.call('get_payer_rme_most_recent_results')
    roster_job_results = anvil.server.call('get_most_recent_roster_jobs')
    print(roster_job_results)
    print('---')

    LAST_RME_RUN_TEXT = 'Last RME Ran On: '
    LAST_RME_COUNT_TEXT = 'Last RME Load Patient Count: '
    LAST_RME_FILENAME_TEXT = 'Latest PROD-ODB File: '
    LAST_RME_COUNT_TEXT = '# of Patients: '
    MOST_RECENT_ROSTER_DOWNLOADED = 'Most Recent Roster Downloaded: '
    LAST_ROSTER_INGESTED = 'Previous Roster Ingested: '
    LAST_ROSTER_DOWNLOADED = 'Last Roster Downloaded: '
    
    '''
    ACO Reach
    -------------------------
    RME
    '''  
    self.item['ACO Reach Previous RME Filename'] = str(NotImplemented) 
    self.item['ACO Reach Previous RME Count'] = LAST_RME_COUNT_TEXT + str(roster_rme_results['ACO Reach']['Count'])
    self.item['ACO Reach Previous RME Date'] = LAST_RME_RUN_TEXT + roster_rme_results['ACO Reach']['Date'].strftime("%Y-%m-%d")

    '''
    Everything Else
    '''
    #some payers have more than one input roster
    for roster_filename in roster_job_results['ACO Reach Roster']['input_files']:
      roster_filename_text = roster_filename + ' '
    print(f'rft: {roster_filename_text}')
    
    self.item['ACO Reach Previous Roster Downloaded'] = LAST_ROSTER_DOWNLOADED + anvil.server.call('get_most_recent_ACO_Reach_roster_downloaded')
    self.item['ACO Reach Previous Roster Ingested'] = LAST_ROSTER_INGESTED + roster_filename_text
    
    
    print('***')
    


    
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
