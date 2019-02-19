"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta

##############################
# Start - Global Code Block

import random
import datetime

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
    url = ['www.badlink.com'
          ]

    for i in range(len(eTo)):
        raw = {}
        cef = {}
        emailHeader = {'Delivered-To': 'company@phishing.com',
           'From': efrom[i],
           'Detected-URL':random.choice(url),
           'Return-Path': '<bounce+07b9a7.9c403',
           'ARC-Seal': '''i=1; a=rsa-sha256; t=1529885666; cv=none; d=google.com; s=arc-20160816; b=CQpzLQywzGbo1pRGG98Ja4x2FTL8ubfppNQg5BFWZLjYkqJOcvJMITXbBt0Jafvb9O
 i5LC/9Yf5jstXwDKHJUYKkuK40+NiAPFmag/G3+CF01Z7EDHMrnsPQ/6EI29jEES6nxg aWGZhbSiISz6OMVpRfUFztR0SAciSaOWCEiD8lQNhCiq6zWHIEJknYhTegsu/Ud8wTI+
 QW91ixIjMJYpOz+SQhMR0QoWn3n7anF1Ny8HEGOKdxirCKE33otb8BGnJif1eH+tzVVQ Lbv4bfyXgJB7QBJgsDCF7YVWicENGuI04KJkPumDZfAFQ7hcBPcV293Bs/ptSI6NyONu
 +izQ==''',
            'To': eTo[i],
            'X-Mailgun-Sending-Ip': '209.61.151.222',
            'X-Mailgun-Tag': 'summary',
            'X-Received':'by 2002:aca:a94c:: with SMTP id s73-v6mr5539575oie.178.1529885666213; Sun, 24 Jun 2018 17:14:26 -0700 (PDT)',
            'ARC-Authentication-Results': 'i=1; mx.google.com; dkim=pass header.i=@mxtoolbox.com header.s=mailo header.b=LY45x805; dkim=pass header.i=@mailgun.org header.s=mg header.b=CorTHVEY; spf=pass (google.com: domain of bounce+07b9a7.9c403-iceburgnotify=gmail.com@mxtoolbox.com designates 209.61.151.222 as permitted sender) smtp.mailfrom="bounce+07b9a7.9c403-iceburgnotify=gmail.com@mxtoolbox.com"; dmarc=pass (p=NONE sp=NONE dis=NONE) header.from=mxtoolbox.com',
            'ARC-Message-Signature':'i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20160816; h=mime-version:subject:from:to:message-id:sender:date:dkim-signature :dkim-signature:arc-authentication-results; bh=To1beBo/++WeZttsCE1s+J+qd8OV0VKh759cYATpGwo=; b=ad0TyCFyaVF2pIjMSD8yO6FCH5ZAT+Cxy8NVYshD0wwUCwaXwt7wIjE1IbzhA18Fz1 sgs8fKHQUMyXOmI6CNShzFyhFwzvk/bsetZTtoHxF0W9P72gu5ufSDRmiCovvrGA181N 0csKaQRemuCml+fxIVjtxui/eG0YKycCAr/J937yLZMNuvXyEJqUbhzo1E2jLMEdAIiN jyx3UYjdaO4hRgAn0IUDUMUhNdhVA8MQwi9uTBSHX63Q7m5ke5fPkfakd1sigpI0s63a 3hk1wjVRv84fn9te/Wf7EaFQVrgJ7T7mn4vPGdujLU9iduzklYlzXlPNw3WBSlZGVKJ2 AazA==',
            'Date':'',
            'Message-Id': '<20180625001424.1.3D7FC1E792BF8A72>',
            'Mime-Version':'1.0',
            'X-Mailgun-Sid':'WyI3MTUwMyIsICJpY2VidXJnbm90aWZ5QGdtYWlsLmNvbSIsICI5YzQwMyJd',
            'Received':'by 2002:ac0:8806:0:0:0:0:0 with SMTP id g6-v6csp3401947img; Sun, 24 Feb 2019, from rs222.mailgun.us (rs222.mailgun.us. [209.61.151.222]) with UTF8SMTPS id d39-v6si4713992otj.152.2018.06.24.17.14.25 (version=TLS1_2 cipher=ECDHE-RSA-AES128-GCM-SHA256 bits=128/128); Sun, 24 Jun 2018 17:14:26 -0700 (PDT), by luna.mailgun.net with HTTP; Mon, 25 Jun 2018 00:14:24 +0000',
            'Received-SPF':'pass client-ip=209.61.151.222;',
            'Sender':efrom[i],
            'Authentication-Results':'''header.s=mailo header.b=LY45x805; dkim=pass header.i=@mailgun.org header.s=mg header.b=CorTHVEY; spf=pass  smtp.mailfrom="bounce+07b9a7.9c403-iceburgnotify=gmail.com@mxtoolbox.com"; dmarc=pass (p=NONE sp=NONE dis=NONE)', 'DKIM-Signature':'a=rsa-sha256; v=1; c=relaxed/relaxed; d=mailgun.org; q=dns/txt; s=mg; t=1529885665; h=Content-Type: Mime-Version: Subject: From: To: Message-Id: Sender: Date: X-Feedback-Id; bh=To1beBo/++WeZttsCE1s+J+qd8OV0VKh759cYATpGwo=; b=CorTHVEYKdaXjjIua05kaOQ+n90uGMEy+rhlg/5L2W9SmusSRFtLlm4rNdXCub6PQD9PjQhp T3/4NanN9ftDgRlOd1U3l33gN2rJf4x92Ytz/vjLKJOg73JbUJYyRxT9pKP6GBk3XK+MkxPD ZI03CSmfX2Dz3pbNibRcUWvhFH8=''',
            'X-Feedback-Id':'5266b068fea3983e6007cc1a:mailgun',
            'Content-Type':'multipart/alternative; boundary="917d6539ef9143b1b76d94c66a93a3bf"',
            'X-Google-Smtp-Source':'ADUXVKJS4kPPUt/4ky1gQgzF2sD9anlyTDaGRxkf6N9q6KOI3wFA2tzA4GwefhlVxyjO3V/+dPte',
            'Subject':'Phishing'            
           }
        cef['emailHeader'] = emailHeader
        cef['fromEmail']=efrom[i]
        cef['toEmail']=eTo[i]
        success, message, artifact_id = phantom.add_artifact(
            container=container, raw_data=raw, cef_data=cef, label='artifact',
            name= 'Reported by: ' + efrom[i], severity='high',
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