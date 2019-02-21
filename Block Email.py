"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'block_sender_1' block
    block_sender_1(container=container)

    return

def call_api_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('call_api_1() called')
    phantom.debug(results)
    return

def whois_domain_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('whois_domain_1() called')

    # collect data for 'whois_domain_1' call

    parameters = []
    
    # build parameters list for 'whois_domain_1' call
    parameters.append({
        'domain': "paypal.account.myorder-manage.com",
    })

    phantom.act("whois domain", parameters=parameters, assets=['passivetotal'], callback=call_api_1, name="whois_domain_1")

    return

def call_api_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('call_api_2() called')
    phantom.debug(results)
    return

def block_sender_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('block_sender_1() called')

    # collect data for 'block_sender_1' call

    parameters = []
    
    # build parameters list for 'block_sender_1' call
    parameters.append({
        'id': "<VI1P175MB0191ABD0857E66DFE334698CBA7E0@VI1P175MB0191.EURP175.PROD.OUTLOOK.COM>",
        'move_to_junk_folder': "",
        'email': "",
    })

    phantom.act("block sender", parameters=parameters, assets=['qualys ingestion'], callback=call_api_2, name="block_sender_1")

    return

def get_screenshot_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('get_screenshot_1() called')

    # collect data for 'get_screenshot_1' call

    parameters = []
    
    # build parameters list for 'get_screenshot_1' call
    parameters.append({
        'url': "https://paypal.account.myorder-manage.com",
        'size': "",
    })

    phantom.act("get screenshot", parameters=parameters, assets=['test ss'], name="get_screenshot_1")

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