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
    test = '''{u'Delivered-To': u'{}', u'From': u'"{}" <support@akamai.com>', u'Return-Path': u'<support=akamai.com__9m4vlv27x6v0rxwe@mmh2xurvokdh.a-hu5amac.na63.bnc.salesforce.com>', u'ARC-Seal': u'i=1; a=rsa-sha256; t=1529913495; cv=none;\r\n        d=google.com; s=arc-20160816;\r\n        b=MpEXpwp1ukpMJLd7c3a3eRWayyg/iNRpYTnfclrI9EzjVl9Mu0pQ3Sa25ZXjTfrCmV\r\n         t5DqWIZDVRiDTBGgXhwNkRf9XApZihkh36YbWIKsRfc6iOFFHpAkcyHv1cSmx7qm+pNs\r\n         UH+i+DeYIsNI0DhQWoYfb59yI6Aep5NeIN2OmQ3IyjwjsHn1th3yoP6Jx7gyVR6Z2agI\r\n         3g6sw5CZ8eICGvNz5ARTVPpvCxX8qTYWU4pbJG85z5qhkmfeJruvGnjbFrIOc3k0qKD/\r\n         C8xeSJyhi8nuFrgXzewx1kCLMS0+lRMboZYap4tX+QdJZWOTF6WRJEXpqq2+CLJVglrE\r\n         vItw==', u'X-mail_abuse_inquiries': u'{}', u'X-SFDC-LK': u'00DA0000000Hu5a', u'X-Sender': u'postmaster@salesforce.com', u'To': u'"{}', u'Message-ID': u'<skIrx000000000000000000000000000000000000000000000PAVCT200AiHXhSo9TYGcWUAWOiNBfA@sfdc.net>', u'X-SFDC-TLS-NoRelay': u'1', u'X-Received': u'by 2002:a62:642:: with SMTP id 63-v6mr12030203pfg.222.1529913495092;\r\n        Mon, 25 Jun 2018 00:58:15 -0700 (PDT)', u'ARC-Authentication-Results': u'i=1; mx.google.com;\r\n       dkim=pass header.i=@akamai.com header.s=sfcrm header.b="NE/ESjZ5";\r\n       spf=pass (google.com: domain of support=akamai.com__9m4vlv27x6v0rxwe@mmh2xurvokdh.a-hu5amac.na63.bnc.salesforce.com designates 136.147.46.214 as permitted sender) smtp.mailfrom="support=akamai.com__9m4vlv27x6v0rxwe@mmh2xurvokdh.a-hu5amac.na63.bnc.salesforce.com";\r\n       dmarc=pass (p=QUARANTINE sp=NONE dis=NONE) header.from=akamai.com', u'ARC-Message-Signature': u'i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816;\r\n        h=mime-version:subject:message-id:to:from:date:dkim-signature\r\n         :arc-authentication-results;\r\n        bh=eBSdjda4b42/4n91LlIwHmGhdSVr7jmsQyrpCoh2cGs=;\r\n        b=M7iARQRFS2PHJutnGioqhiajV/5QpHtrV+5WJeylxCzmCn3quhLzeDSFsn3oPRx9+C\r\n         JrzJVXAg5LmokhOqzHQ0rUnXNpgqYTnPyVa6+nvyJb//SVfYcVch/u74kX7I7grJcXa5\r\n         CeYmK6NXyYaHfuz1wPcYvoyCheHmOTqH4bQ62gNZ85ykAhX9aNZqK+PqaT+e0csLdRCa\r\n         JDr3dWuwJ4Dz2QNDXzJG1pBLer2tDlRF3kyn9mwdq39r/0we54QSlTaoW1QafaSeHJ0Z\r\n         gtWtpiDjg0ABih7fiKgP7WjwojbZpm7vDFajxf5sklw+W55UScnELFRNE01TRj1MW6Ow\r\n         0llA==', u'Date': u'Mon, 25 Jun 2018 07:58:14 +0000 (GMT)', u'Received': [u'by 2002:ac0:8806:0:0:0:0:0 with SMTP id g6-v6csp3707963img;\r\n        Mon, 25 Jun 2018 00:58:15 -0700 (PDT)', u'from smtp07-phx-sp3.mta.salesforce.com (smtp07-phx-sp3.mta.salesforce.com. [136.147.46.214])\r\n        by mx.google.com with ESMTPS id r3-v6si11315757pgf.339.2018.06.25.00.58.14\r\n        for <iceburgnotify@gmail.com>\r\n        (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128);\r\n        Mon, 25 Jun 2018 00:58:15 -0700 (PDT)', u'from [10.220.8.170] ([10.220.8.170:57856] helo=na63-app2-15-phx.ops.sfdc.net)\r\n\tby mx3-phx-sp3.mta.salesforce.com (envelope-from <support=akamai.com__9m4vlv27x6v0rxwe@mmh2xurvokdh.a-hu5amac.na63.bnc.salesforce.com>)\r\n\t(ecelerity 3.6.25.63389 r(Core:tip)) with ESMTPS (cipher=ECDHE-RSA-AES256-GCM-SHA384) \r\n\tid AD/92-34703-690A03B5; Mon, 25 Jun 2018 07:58:14 +0000'], u'Received-SPF': u'pass (google.com: domain of support=akamai.com__9m4vlv27x6v0rxwe@mmh2xurvokdh.a-hu5amac.na63.bnc.salesforce.com designates 136.147.46.214 as permitted sender) client-ip=136.147.46.214;', u'Authentication-Results': u'mx.google.com;\r\n       dkim=pass header.i=@akamai.com header.s=sfcrm header.b="NE/ESjZ5";\r\n       spf=pass (google.com: domain of support=akamai.com__9m4vlv27x6v0rxwe@mmh2xurvokdh.a-hu5amac.na63.bnc.salesforce.com designates 136.147.46.214 as permitted sender) smtp.mailfrom="support=akamai.com__9m4vlv27x6v0rxwe@mmh2xurvokdh.a-hu5amac.na63.bnc.salesforce.com";\r\n       dmarc=pass (p=QUARANTINE sp=NONE dis=NONE) header.from=akamai.com', u'X-SFDC-EmailCategory': u'emailPublisherEmail', u'X-SFDC-Binding': u'1WrIRBV94myi25uB', u'X-SFDC-User': u'0050f000008V82Z', u'MIME-Version': u'1.0', u'X-SFDC-EntityId': u'5000f00001JDgI4', u'DKIM-Signature': u'v=1; a=rsa-sha256; c=relaxed/simple; d=akamai.com; s=sfcrm;\r\n\tt=1529913494; bh=eBSdjda4b42/4n91LlIwHmGhdSVr7jmsQyrpCoh2cGs=;\r\n\th=Date:From:To:Subject:MIME-Version:Content-Type;\r\n\tb=NE/ESjZ5xHSUd0nt9xUgrLB6hNQVllZZIIZ2wsAS5MoV8n4QxNdW5kEoduSYCvMoa\r\n\t fSb2FAP5sv22jmGVYLkbZE9kZWDq/EAAP4BBWvp5INZ69bXsk69VRnkwI7fANovY8X\r\n\t Bm9Hh8gL0b+8hncQe80lxph4UGEdCIJ3BSEa3RlE=', u'Subject': u'[AKAM-CASE #F-CS-2849177] RE: Account Creation Assistance', u'Content-Type': u'multipart/alternative; \r\n\tboundary="----=_Part_2556_81079253.1529913494635"', u'X-Google-Smtp-Source': u'ADUXVKIv4rqsLaCcBd3SbmmlyCbBkCNuE9pAAVLMQ1uuxP8aKesFKlexobH67pG9L39P22UKOzQL', u'X-SFDC-Interface': u'internal'}'''.format('to@test.com','from@test.com','urlww.url','to@test.com')
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