"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'create_ticket' block
    create_ticket(container=container)

    return

def create_ticket(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('create_ticket() called')

    # collect data for 'create_ticket' call

    parameters = []
    
    # build parameters list for 'create_ticket' call
    parameters.append({
        'short_description': "Block URL",
        'description': "Request to block url",
        'table': "incident",
        'fields': "",
        'vault_id': "",
    })

    phantom.act("create ticket", parameters=parameters, assets=['servicenow'], callback=details, name="create_ticket")

    return

def details(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('details() called')
    phantom.debug(results)
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