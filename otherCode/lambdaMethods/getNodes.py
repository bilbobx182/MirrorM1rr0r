import json


def lambda_handler(event, context):
    result = {"nodes": [
        {
            "title": "help",
            "Description": "This returns a list of nodes with descriptions",
            "Parameters": "N/A",
            "Return": "List of type nodes"
        },
        {
            "title": "getMessage",
            "Description": "Returns JSON for given message in the queue",
            "Parameters": "queueurl, count",
            "ParametersDesc": "A url to a queue, the count of messages wanted (optional)",
            "Return": "Message"
        },
        {
            "title": "createFIFOQueue",
            "Description": "Creates a queue in AWS SQS so that the mirror can pull from it",
            "Parameters": "queueName",
            "ParametersDesc": "A a unique hashed string that will then be used as the queue name",
            "Return": "queueurl"
        },
        {
            "title": "sendFifoMessage",
            "Description": "Send a message to a queue via query parameters",
            "Parameters": "queueurl,message,location(optional),fontsize(optional),fontcolour(optional)",
            "ParametersDesc": "the queue you want to send to, stringified message you want to send, x and y location denoted as 'x,y' ie 1,1, a numeric value for how big you want the font, Hex colour value for font colour",
            "Return": "String of status",
            "ErrorMessage": "Queue or message payload were not passed :(",
            "ErrorDescription": "You didn't pass the query parameters of the queueurl correctly, or message correctly"
        },
        {
            "title": "sendFIFOMessagePOST",
            "Description": "Same as sending a message except via a post request",
            "Parameters": "Sample in the github repo under PostSample.json",
            "ParametersDesc": "queueurl holds the queue, data holds the payload that you want to send to a queue",
            "Return": "String of status",
            "ErrorMessage": "Queue or message payload were not passed :(",
            "ErrorDescription": "You didn't pass the query parameters of the queueurl correctly, or message correctly"
        }
    ]
    }
    outJSON = {}
    outJSON['statusCode'] = 200
    outJSON['body'] = json.dumps(result)

    outJSON['headers'] = {
        "content-type": "application-json"
    }
    return (outJSON)