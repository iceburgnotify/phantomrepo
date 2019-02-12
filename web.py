"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

import requests, bs4

# End - Global Code block
##############################

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'webscrapping' block
    webscrapping(container=container)

    return

def webscrapping(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('webscrapping() called')
    response = requests.get("https://en.wikipedia.org/wiki/List_of_Olympic_medalists_in_judo")	
    htmlResponse = bs4.BeautifulSoup(response.text)
    table = htmlResponse.select('table')
    tbody = table[0].select('tbody')
    phantom.debug(tbody)
    
    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all detals of actions 
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return