"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

url = 'https://paypal.account.myorder-manage.com/signin/'

# End - Global Code block
##############################

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'url_reputation' block
    url_reputation(container=container)

    return

def url_reputation(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('url_reputation() called')

    # collect data for 'url_reputation' call

    parameters = []
    
    # build parameters list for 'url_reputation' call
    parameters.append({
        'url': "",
    })

    phantom.act("url reputation", parameters=parameters, assets=['virustotal'], name="url_reputation")

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