from .utils import Data
from .utils.Navigation import navigate
from anvil import set_default_error_handling
import anvil.users
from anvil import *

# On Authentication failure, navigates back to login back. Throw error as usual for any other type of error
def error_handler(err):
  if isinstance(err, anvil.users.exceptions.AuthenticationFailed):
    open_form('Components.Autocomplete')
    #navigate(page='arrival')
  else:
    raise err
set_default_error_handling(error_handler)

def start_up():
  open_form('Components.Autocomplete')
  #navigate("arrival")
  #Data.get_initial_data()
    

if __name__ == "__main__":
  start_up()