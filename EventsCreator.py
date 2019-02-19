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
    test = '''{'Delivered-To': '{}', 'From': '"{}" <spport@akamai.com>', 'Retrn-Path': '<spport=akamai.com__9m4vlv27x6v0rxwe@mmh2xrvokdh.a-h5amac.na63.bnc.salesforce.com>', 'ARC-Seal': 'i=1; a=rsa-sha256; t=1529913495; cv=none;\r\n        d=google.com; s=arc-20160816;\r\n        b=MpEXpwp1kpMJLd7c3a3eRWayyg/iNRpYTnfclrI9EzjVl9M0pQ3Sa25ZXjTfrCmV\r\n         t5DqWIZDVRiDTBGgXhwNkRf9XApZihkh36YbWIKsRfc6iOFFHpAkcyHv1cSmx7qm+pNs\r\n         H+i+DeYIsNI0DhQWoYfb59yI6Aep5NeIN2OmQ3IyjwjsHn1th3yoP6Jx7gyVR6Z2agI\r\n         3g6sw5CZ8eICGvNz5ARTVPpvCxX8qTYW4pbJG85z5qhkmfeJrvGnjbFrIOc3k0qKD/\r\n         C8xeSJyhi8nFrgXzewx1kCLMS0+lRMboZYap4tX+QdJZWOTF6WRJEXpqq2+CLJVglrE\r\n         vItw==', 'X-mail_abse_inqiries': '{}', 'X-SFDC-LK': '00DA0000000H5a', 'X-Sender': 'postmaster@salesforce.com', 'To': '"{}', 'Message-ID': '<skIrx000000000000000000000000000000000000000000000PAVCT200AiHXhSo9TYGcWAWOiNBfA@sfdc.net>', 'X-SFDC-TLS-NoRelay': '1', 'X-Received': 'by 2002:a62:642:: with SMTP id 63-v6mr12030203pfg.222.1529913495092;\r\n        Mon, 25 Jn 2018 00:58:15 -0700 (PDT)', 'ARC-Athentication-Reslts': 'i=1; mx.google.com;\r\n       dkim=pass header.i=@akamai.com header.s=sfcrm header.b="NE/ESjZ5";\r\n       spf=pass (google.com: domain of spport=akamai.com__9m4vlv27x6v0rxwe@mmh2xrvokdh.a-h5amac.na63.bnc.salesforce.com designates 136.147.46.214 as permitted sender) smtp.mailfrom="spport=akamai.com__9m4vlv27x6v0rxwe@mmh2xrvokdh.a-h5amac.na63.bnc.salesforce.com";\r\n       dmarc=pass (p=QARANTINE sp=NONE dis=NONE) header.from=akamai.com', 'ARC-Message-Signatre': 'i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;\r\n        h=mime-version:sbject:message-id:to:from:date:dkim-signatre\r\n         :arc-athentication-reslts;\r\n        bh=eBSdjda4b42/4n91LlIwHmGhdSVr7jmsQyrpCoh2cGs=;\r\n        b=M7iARQRFS2PHJtnGioqhiajV/5QpHtrV+5WJeylxCzmCn3qhLzeDSFsn3oPRx9+C\r\n         JrzJVXAg5LmokhOqzHQ0rnXNpgqYTnPyVa6+nvyJb//SVfYcVch/74kX7I7grJcXa5\r\n         CeYmK6NXyYaHfz1wPcYvoyCheHmOTqH4bQ62gNZ85ykAhX9aNZqK+PqaT+e0csLdRCa\r\n         JDr3dWwJ4Dz2QNDXzJG1pBLer2tDlRF3kyn9mwdq39r/0we54QSlTaoW1QafaSeHJ0Z\r\n         gtWtpiDjg0ABih7fiKgP7WjwojbZpm7vDFajxf5sklw+W55ScnELFRNE01TRj1MW6Ow\r\n         0llA==', 'Date': 'Mon, 25 Jn 2018 07:58:14 +0000 (GMT)', 'Received': ['by 2002:ac0:8806:0:0:0:0:0 with SMTP id g6-v6csp3707963img;\r\n        Mon, 25 Jn 2018 00:58:15 -0700 (PDT)', 'from smtp07-phx-sp3.mta.salesforce.com (smtp07-phx-sp3.mta.salesforce.com. [136.147.46.214])\r\n        by mx.google.com with ESMTPS id r3-v6si11315757pgf.339.2018.06.25.00.58.14\r\n        for <icebrgnotify@gmail.com>\r\n        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);\r\n        Mon, 25 Jn 2018 00:58:15 -0700 (PDT)', 'from [10.220.8.170] ([10.220.8.170:57856] helo=na63-app2-15-phx.ops.sfdc.net)\r\n\tby mx3-phx-sp3.mta.salesforce.com (envelope-from <spport=akamai.com__9m4vlv27x6v0rxwe@mmh2xrvokdh.a-h5amac.na63.bnc.salesforce.com>)\r\n\t(ecelerity 3.6.25.63389 r(Core:tip)) with ESMTPS (cipher=ECDHE-RSA-AES256-GCM-SHA384) \r\n\tid AD/92-34703-690A03B5; Mon, 25 Jn 2018 07:58:14 +0000'], 'Received-SPF': 'pass (google.com: domain of spport=akamai.com__9m4vlv27x6v0rxwe@mmh2xrvokdh.a-h5amac.na63.bnc.salesforce.com designates 136.147.46.214 as permitted sender) client-ip=136.147.46.214;', 'Athentication-Reslts': 'mx.google.com;\r\n       dkim=pass header.i=@akamai.com header.s=sfcrm header.b="NE/ESjZ5";\r\n       spf=pass (google.com: domain of spport=akamai.com__9m4vlv27x6v0rxwe@mmh2xrvokdh.a-h5amac.na63.bnc.salesforce.com designates 136.147.46.214 as permitted sender) smtp.mailfrom="spport=akamai.com__9m4vlv27x6v0rxwe@mmh2xrvokdh.a-h5amac.na63.bnc.salesforce.com";\r\n       dmarc=pass (p=QARANTINE sp=NONE dis=NONE) header.from=akamai.com', 'X-SFDC-EmailCategory': 'emailPblisherEmail', 'X-SFDC-Binding': '1WrIRBV94myi25B', 'X-SFDC-ser': '0050f000008V82Z', 'MIME-Version': '1.0', 'X-SFDC-EntityId': '5000f00001JDgI4', 'DKIM-Signatre': 'v=1; a=rsa-sha256; c=relaxed/simple; d=akamai.com; s=sfcrm;\r\n\tt=1529913494; bh=eBSdjda4b42/4n91LlIwHmGhdSVr7jmsQyrpCoh2cGs=;\r\n\th=Date:From:To:Sbject:MIME-Version:Content-Type;\r\n\tb=NE/ESjZ5xHSd0nt9xgrLB6hNQVllZZIIZ2wsAS5MoV8n4QxNdW5kEodSYCvMoa\r\n\t fSb2FAP5sv22jmGVYLkbZE9kZWDq/EAAP4BBWvp5INZ69bXsk69VRnkwI7fANovY8X\r\n\t Bm9Hh8gL0b+8hncQe80lxph4GEdCIJ3BSEa3RlE=', 'Sbject': '[AKAM-CASE #F-CS-2849177] RE: Accont Creation Assistance', 'Content-Type': 'mltipart/alternative; \r\n\tbondary="----=_Part_2556_81079253.1529913494635"', 'X-Google-Smtp-Sorce': 'ADXVKIv4rqsLaCcBd3SbmmlyCbBkCNE9pAAVLMQ1xP8aKesFKlexobH67pG9L39P22KOzQL', 'X-SFDC-Interface': 'internal'}'''.format('to@test.com','from@test.com','urlww.url','to@test.com')
    cef['emailHeader'] = test

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