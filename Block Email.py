"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'run_query_2' block
    run_query_2(container=container)

    return

def whois_domain_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('whois_domain_1() called')

    # collect data for 'whois_domain_1' call

    parameters = []
    
    # build parameters list for 'whois_domain_1' call
    parameters.append({
        'domain': "paypal.account.myorder-manage.com",
    })

    phantom.act("whois domain", parameters=parameters, assets=['passivetotal'], name="whois_domain_1")

    return

def Block_Email_Result(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('call_api_2() called')
    phantom.debug("Successfully blocked the email")
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

def call_api_3(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('call_api_3() called')
    phantom.debug(results)
    return

def send_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('send_email_1() called')

    # collect data for 'send_email_1' call

    parameters = []
    
    # build parameters list for 'send_email_1' call
    parameters.append({
        'body': "this is testing",
        'to': "soartesting2019@outlook.com",
        'from': "gonnastopus@outlook.com",
        'attachments': "",
        'subject': "test delete",
    })

    phantom.act("send email", parameters=parameters, assets=['smtp'], name="send_email_1")

    return

def call_api_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('call_api_1() called')
    phantom.debug(results)
    return

def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('run_query_1() called')

    # collect data for 'run_query_1' call

    parameters = []
    
    # build parameters list for 'run_query_1' call
    parameters.append({
        'body': "",
        'internet_message_id': "",
        'sender': "",
        'ignore_subfolders': "",
        'range': "0-10",
        'query': "",
        'folder': "Inbox",
        'email': "iceburgnotify@gmail.com",
        'subject': "",
    })

    phantom.act("run query", parameters=parameters, app={ "name": 'EWS for Office 365' }, name="run_query_1")

    return

def get_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('get_email_1() called')

    # collect data for 'get_email_1' call

    parameters = []
    
    # build parameters list for 'get_email_1' call
    parameters.append({
        'ingest_email': "",
        'container_id': 1734,
        'vault_id': "",
        'id': "",
        'email': "",
    })

    phantom.act("get email", parameters=parameters, assets=['office365'], callback=delete_email_1, name="get_email_1")

    return

def delete_email_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('delete_email_1() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'delete_email_1' call

    parameters = []
    
    # build parameters list for 'delete_email_1' call
    parameters.append({
        'id': "AQMkADAwATM3ZmYAZS0xZTcwLTYxZGQALTAwAi0wMAoARgAAA8sbs2bgxWhOm/D/136MLx0HAHgHnxYkWTlOk6pq0IWFAMxLAAACAQwAAAB4B58WJFk5TpOqatCFhQDMSwAAAAyVhDsAAAA=",
        'email': "",
    })

    phantom.act("delete email", parameters=parameters, assets=['office365'], callback=call_api_1, name="delete_email_1", parent_action=action)

    return

def block_sender_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('block_sender_1() called')

    # collect data for 'block_sender_1' call

    parameters = []
    
    # build parameters list for 'block_sender_1' call
    parameters.append({
        'id': "AQMkADAwATM3ZmYAZS0xZTcwLTYxZGQALTAwAi0wMAoARgAAA8sbs2bgxWhOm/D/136MLx0HAHgHnxYkWTlOk6pq0IWFAMxLAAACAQwAAAB4B58WJFk5TpOqatCFhQDMSwAAAAyVhDwAAAA=",
        'move_to_junk_folder': "",
        'email': "",
    })

    phantom.act("block sender", parameters=parameters, assets=['office365'], callback=Block_Email_Result, name="block_sender_1")

    return

def delete_email_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('delete_email_2() called')

    parameters = []

    phantom.act("delete email", parameters=parameters, app={ "name": 'EWS for Office 365 Debug' }, name="delete_email_2")

    return

def run_query_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('run_query_2() called')

    # collect data for 'run_query_2' call

    parameters = []
    
    # build parameters list for 'run_query_2' call
    parameters.append({
        'email': "soartesting2019@outlook.com",
        'folder': "Inbox",
        'subject': "test3",
        'sender': "",
        'body': "",
        'internet_message_id': "",
        'query': "",
        'range': "0-10",
        'ignore_subfolders': "",
    })

    phantom.act("run query", parameters=parameters, assets=['office365'], callback=call_api_3, name="run_query_2")

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