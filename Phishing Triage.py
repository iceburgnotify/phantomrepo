"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

url = 'https://paypal.account.myorder-manage.com/signin/'
domain ='paypal.account.myorder-manage.com/signin/'

# End - Global Code block
##############################

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'whois_domain_1' block
    whois_domain_1(container=container)

    return

def vt_url_reputation(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('vt_url_reputation() called')

    # collect data for 'vt_url_reputation' call

    parameters = []
    
    # build parameters list for 'vt_url_reputation' call
    parameters.append({
        'url': "",
    })

    phantom.act("url reputation", parameters=parameters, assets=['virustotal'], callback=pt_url_reputation, name="vt_url_reputation")

    return

def pt_url_reputation(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('pt_url_reputation() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))

    parameters = []

    phantom.act("url reputation", parameters=parameters, app={ "name": 'PhishTank' }, name="pt_url_reputation", parent_action=action)

    return

def whois_domain_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('whois_domain_1() called')

    # collect data for 'whois_domain_1' call

    parameters = []
    
    # build parameters list for 'whois_domain_1' call
    parameters.append({
        'domain': domain,
    })

    phantom.act("whois domain", parameters=parameters, assets=['whois'], callback=call_api_1, name="whois_domain_1", parent_action=action)

    return

def call_api_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('call_api_1() called')
    phantom.debug(results)
    return

def geolocate_ip_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('geolocate_ip_1() called')

    parameters = []

    phantom.act("geolocate ip", parameters=parameters, app={ "name": 'MaxMind' }, name="geolocate_ip_1", parent_action=action)

    return

def lookup_domain_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('lookup_domain_1() called')

    # collect data for 'lookup_domain_1' call

    parameters = []
    
    # build parameters list for 'lookup_domain_1' call
    parameters.append({
        'domain': url,
        'type': "mx",
    })

    phantom.act("lookup domain", parameters=parameters, assets=['mxtoolbox'], callback=call_api_1, name="lookup_domain_1")

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