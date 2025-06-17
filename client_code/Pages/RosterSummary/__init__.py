from ._anvil_designer import RosterSummaryTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
from ...Components.Icons.CheckMark import CheckMark
from ...Components.Icons.RedX import RedX
from ...Components.Icons.Hourglass import Hourglass
from datetime import datetime

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
    previous_payer_data_check_job_results = anvil.server.call('get_previous_data_interface_job_details')

    print(previous_payer_data_check_job_results)
    print('---')

    LAST_RME_RUN_TEXT = 'Last RME Ran On: '
    LAST_RME_COUNT_TEXT = 'Last RME Load Patient Count: '
    LAST_RME_FILENAME_TEXT = 'Latest PROD-ODB File: '
    LAST_RME_COUNT_TEXT = '# of Patients: '
    MOST_RECENT_ROSTER_DOWNLOADED = 'Most Recent Roster Downloaded: '
    LAST_ROSTER_INGESTED = 'Previous Roster Ingested: '
    LAST_ROSTER_DOWNLOADED = 'Last Roster Downloaded: '
    LAST_PAYER_SITE_CHECK = 'Last Check for New Roster on Payer Site: '
    FAIL = 'FAILED TO LOAD DATA'

    print(datetime.now())
    
    '''
    ACO Reach
    -------------------------
    RME
    '''
    try:
      self.item['ACO Reach Previous RME Filename'] = str(NotImplemented) 
    except:
      self.item['ACO Reach Previous RME Filename'] = FAIL

    try:
      self.item['ACO Reach Previous RME Count'] = LAST_RME_COUNT_TEXT + str(roster_rme_results['ACO Reach']['Count'])
    except:
      self.item['ACO Reach Previous RME Count'] = LAST_RME_COUNT_TEXT + FAIL
      
    try:
      self.item['ACO Reach Previous RME Date'] = LAST_RME_RUN_TEXT + roster_rme_results['ACO Reach']['Date'].strftime("%Y-%m-%d")
    except:
      self.item['ACO Reach Previous RME Date'] = LAST_RME_RUN_TEXT + FAIL
      
    try:
      
      self.item['ACO Reach Previous datafiles Check'] = LAST_PAYER_SITE_CHECK + '{date}'.format(date=datetime.strptime(previous_payer_data_check_job_results['datetime'], '%Y-%m-%d %H:%M:%S.%f').strftime( '%Y-%m-%d %H:%M'))
    except:
      self.item['ACO Reach Previous datafiles Check'] = LAST_PAYER_SITE_CHECK + FAIL
    '''
    Everything Else
    '''
    #some payers have more than one input roster
    for roster_filename in roster_job_results['ACO Reach Roster']['input_files']:
      roster_filename_text = roster_filename + ' '
    print(f'rft: {roster_filename_text}')
    try:
      self.item['ACO Reach Previous Roster Downloaded'] = LAST_ROSTER_DOWNLOADED + anvil.server.call('get_most_recent_ACO_Reach_roster_downloaded')
    except:
      pass
    try:
      self.item['ACO Reach Previous Roster Ingested'] = LAST_ROSTER_INGESTED + FAIL
    except:
      self.item['ACO Reach Previous Roster Ingested'] = LAST_ROSTER_INGESTED + FAIL
      
    
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

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('start_job_schedule')
