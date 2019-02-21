"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

url = 'https://paypal.account.myorder-manage.com/signin/'
domain ='paypal.account.myorder-manage.com'

# End - Global Code block
##############################

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'vt_url_reputation' block
    vt_url_reputation(container=container)

    return

def promote_to_case(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('promote_to_case() called')
    vt_result = phantom.collect2(container=container,datapath=['vt_url_reputation:action_result.data.*.positives'],action_results=results)
    if vt_result:
        positive = vt_result[0][0]
        if positive>0:
            phantom.promote(container=container, template="Phishing Playbook")

    return

def vt_url_reputation(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('vt_url_reputation() called')
    
    # collect data for 'vt_url_reputation' call

    parameters = []
    
    # build parameters list for 'vt_url_reputation' call
    parameters.append({
        'url': url
    })

    phantom.act("url reputation", parameters=parameters, assets=['virustest'], callback=pt_url_reputation, name="vt_url_reputation")

    return

def whois_ip_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('whois_ip_1() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'whois_ip_1' call

    parameters = []
    
    # build parameters list for 'whois_ip_1' call
    parameters.append({
        'ip': "146.112.251.231",
    })

    phantom.act("whois ip", parameters=parameters, app={ "name": 'PassiveTotal' }, callback=pt_url_reputation, name="whois_ip_1", parent_action=action)

    return

def pt_url_reputation(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('pt_url_reputation() called')
    if not success:
        phantom.debug('Error in url reputation of VirusTotal')
        return
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    phantom.debug(results)
    # collect data for 'pt_url_reputation' call

    parameters = []
    
    # build parameters list for 'pt_url_reputation' call
    parameters.append({
        'url': url,
    })

    phantom.act("url reputation", parameters=parameters, assets=['phishtank'], callback=geolocate_ip, name="pt_url_reputation", parent_action=action)

    return

def whois_domain_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('whois_domain_1() called')
    if not success:
        phantom.debug('Error in geolocate ip of MaxMind')
        return
    # collect data for 'whois_domain_1' call
    phantom.debug(results)
    parameters = []
    
    # build parameters list for 'whois_domain_1' call
    parameters.append({
        'domain': domain,
    })

    phantom.act("whois domain", parameters=parameters, assets=['whois'], callback=get_screenshot_1, name="whois_domain_1", parent_action=action)

    return

def geolocate_ip(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('geolocate_ip() called')
    if not success:
        phantom.debug('Error in url reputation of PhishTank')
        return
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    phantom.debug(results)
    # collect data for 'geolocate_ip' call

    parameters = []
    
    # build parameters list for 'geolocate_ip' call
    parameters.append({
        'ip': "146.112.251.231",
    })

    phantom.act("geolocate ip", parameters=parameters, assets=['maxmind'], callback=whois_domain_1, name="geolocate_ip", parent_action=action)

    return

def get_screenshot_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('get_screenshot_1() called')
    if not success:
        phantom.debug('Error in checking domain of whois')
        return
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    phantom.debug(results)
    # collect data for 'get_screenshot_1' call

    parameters = []
    
    # build parameters list for 'get_screenshot_1' call
    parameters.append({
        'url': "http://eden.it-guys.net.nz/wp-content/languages/plugins/ugh/Entrar/Login",
        'size': "",
    })

    phantom.act("get screenshot", parameters=parameters, assets=['test ss'], callback=promote_to_case, name="get_screenshot_1", parent_action=action)

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