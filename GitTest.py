"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'lookup_domain_1' block
    lookup_domain_1(container=container)

    return

def lookup_domain_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('lookup_domain_1() called')

    # collect data for 'lookup_domain_1' call

    parameters = []
    
    # build parameters list for 'lookup_domain_1' call
    parameters.append({
        'domain': "8.8.8.8",
        'type': "mx",
    })

    phantom.act("lookup domain", parameters=parameters, app={ "name": 'MxToolbox' }, callback=call_api_1, name="lookup_domain_1")

    return

def call_api_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('call_api_1() called')
    phantom.debug('testq')
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