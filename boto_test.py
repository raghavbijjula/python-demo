#!/usr/bin/env python
import boto3
from botocore.exceptions import ClientError

def test():
    CONFIGURATION_SET = 'ConfigSet'
    CHARSET = "UTF-8"
    SENDER = "noreply-checkpoint@thomsonreuters.com"
    RECIPIENT = "rbijjula@thomsonreuters.com"
    AWS_REGION = "us-east-1"
    SUBJECT = "AWS SES Test email with links"
    BODY_HTML = """<html>
    <head></head>
    <body>
        <h1>Amazon SES SMTP Email Test</h1>
            <p>This email was sent with Amazon SES using the
            <a href='https://www.python.org/'>Python</a>
            <a href='https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#client'>
            boto3</a> library.</p>
    </body>
    </html>
    """
    client = boto3.client('ses',region_name=AWS_REGION)
    response = client.send_email(
        Destination={
            'ToAddresses': [
                RECIPIENT,
            ],
        },
        Message={
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': BODY_HTML,
                }
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': SUBJECT,
            },
        },
        Source=SENDER,
        ConfigurationSetName=CONFIGURATION_SET
    )

    print(response['MessageId'])
def main():
    test()

if __name__ == '__main__':
   main()
