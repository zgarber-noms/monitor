from ._anvil_designer import RosterInformationTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

"""
    A form meant to be embedded used to fill out the roster information of the payers on the payer screen tab

    Attributes
    ----------
    rosterDownloaded : dict
        Holds information about the last file downloaded
    rosterIngested : dict
        Hold information about last file 
    
    Methods
    -------
    area() : float
        Calculates the area of the rectangle
    perimeter() : float
        Calculates the perimeter of the rectangle
    """
class RosterInformation(RosterInformationTemplate):
  def __init__(self, rosterDownloaded, rosterIngested, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)


    #self.item is bounded to the UI elements
    self.item['rosterLastDownloadedDate'] = rosterDownloaded['Date']
    self.item['rosterLastDownloadedName'] = rosterDownloaded['Name']
    self.item['rosterLastDownloadedSize'] = rosterDownloaded['Size']

    self.item['rosterLastDownloadedDate'] = rosterDownloaded['Date']
    self.item['rosterLastDownloadedName'] = rosterDownloaded['Name']
    self.item['rosterLastDownloadedSize'] = rosterDownloaded['Size']

    
    self.item['rosterLastIngested'] = rosterIngested['']
    self.item['']

    # Any code you write here will run before the form opens.
