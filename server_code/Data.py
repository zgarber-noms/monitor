import anvil.server
from anvil.tables import app_tables
import pandas as pd

CATEGORIES = [(x['name'], x) for x in app_tables.categories.search()]
PRIORITIES = [(x['name'], x) for x in app_tables.priorities.search()]
STATUS = [(x['name'], x) for x in app_tables.status.search()]
OPEN = app_tables.status.get(name="Open")
URGENT = app_tables.priorities.get(name="Urgent")
CLOSED = app_tables.status.get(name="Closed")
OUTGOING = app_tables.types.get(name="OUTGOING_EMAIL")
INTERNAL = app_tables.types.get(name="INTERNAL_NOTE")
INCOMING = app_tables.types.get(name="INCOMING_EMAIL")
CURRENT_TICKET_NO = app_tables.currentticketno.search()[0]['number']
NO_AGENTS_SELECTED = 'None'
NEW_CATEGORY = app_tables.categories.get(name="New")
NEW_PRIORITY = app_tables.priorities.get(name="New")

@anvil.server.callable
def get_initial_data():
  return dict(
    CATEGORIES = CATEGORIES,
    PRIORITIES = PRIORITIES,
    STATUS = STATUS,
    OPEN = OPEN,
    URGENT = URGENT,
    CLOSED = CLOSED,
    OUTGOING = OUTGOING,
    INTERNAL = INTERNAL,
    INCOMING = INCOMING,
    CURRENT_TICKET_NO = CURRENT_TICKET_NO,
    NO_AGENTS_SELECTED = NO_AGENTS_SELECTED,
    NEW_CATEGORY = NEW_CATEGORY,
    NEW_PRIORITY = NEW_PRIORITY
  )

@anvil.server.callable
def df_as_markdown(table, schema):
  print(table)
  print(schema)
  # get the df somehow
  print('called markdown')
  data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'Department': ['Sales', 'Engineering', 'Sales', 'Engineering', 'HR'],
    'Salary': [50000, 75000, 60000, 80000, 55000]
  }
  df = pd.DataFrame(data)
  print(df.shape[0])
  x = df.to_markdown()

  print(x)
  return x
    
