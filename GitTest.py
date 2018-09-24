"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

import xmltodict

def xmltojson():
    retValue = json.loads(json.dumps(xmltodict.parse('''
     <root>
       <persons city="hyderabad">
         <person name="abc">
           <name age="50" mobile="789" />
         </person>
       </persons>
       <persons city="vizag">
            <username></username>
         <person name="xyz">
           <name age="70" mobile="123" />
         </person>
       </persons>
     </root>
     ''')))
    return retValue

# End - Global Code block
##############################

def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'call_api_2' block
    call_api_2(container=container)

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

    phantom.act("lookup domain", parameters=parameters, app={ "name": 'MxToolbox' }, callback=check_url_1, name="lookup_domain_1")

    return

def check_url_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('check_url_1() called')
    
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'check_url_1' call

    parameters = []
    
    # build parameters list for 'check_url_1' call
    parameters.append({
        'url': "q",
    })

    phantom.act("check_url", parameters=parameters, app={ "name": 'NetCraft' }, name="check_url_1", parent_action=action)

    return

def add_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('add_1() called')

    # collect data for 'add_1' call

    parameters = []
    
    # build parameters list for 'add_1' call
    parameters.append({
        'first_numb': "1",
        'second_numb': "2",
    })

    phantom.act("add", parameters=parameters, app={ "name": 'calculator' }, callback=call_api_1, name="add_1")

    return

def call_api_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('call_api_1() called')
    phantom.debug(results)
    return
    return

def call_api_2(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None):
    phantom.debug('call_api_2() called')
    test = xmltojson()
    phantom.debug(test)
    return
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