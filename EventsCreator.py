"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

import random

domains = [ "hotmail.com", "gmail.com", "aol.com", "mail.com" , "mail.kz", "yahoo.com"]
#letters = 'qwertyuiopasdf'.ascii_lowercase[:12]
letters = ["a", "b", "c", "d","e", "f", "g", "h", "i", "j", "k", "l"]
def get_random_domain(domains):
    return random.choice(domains)

def get_random_name(letters, length):
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_emails(nb, length):
    return [get_random_name(letters, length) + '@' + get_random_domain(domains) for i in range(nb)]

# End - Global Code block
##############################

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'add_artifact' block
    add_artifact(container=container)

    return

def add_artifact(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('add_artifact() called')

    efrom = generate_random_emails(20, 7)
    eTo = generate_random_emails(20, 7)

    artifacts = phantom.collect(container, 'artifacts:*', scope='all')
    phantom.debug(artifacts)

    raw = {}
    cef = {}
    cef['sourceAddress'] = '1.1.1.2'

    success, message, artifact_id = phantom.add_artifact(
        container=container, raw_data=raw, cef_data=cef, label='netflow',
        name='test_event', severity='high',
        identifier=None,
        artifact_type='network')
    phantom.debug('artifact added as id:'+str(artifact_id))

    artifacts = phantom.collect(container, 'artifacts:*', scope='all')
    phantom.debug(artifacts)
    
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