import base64
import json
import boto3
import io
from collections import OrderedDict

# Creating our clients for interacting with the AWS services.
ec2_client = boto3.client("ec2")
ec2 = boto3.resource("ec2")


def lambda_handler(event, context):
    """
    This function processes vpc flow log records buffered by Amazon Kinesis Data Firehose. Each record is enriched with additional metadata
    like resource tags for source & destination IP address. VPC ID, Region, Subnet ID, Interface ID etc. for destination IP address.
    This assumes Version 2 fields are being used within the Flow Log Records.
    """

    # Creating empty output list.
    output = []

    # Printing logged event for future reference if ever needed.
    # Comment this out if not needed.
    print(event)

    # Looping through all records pushed into the event. Usually there are multiple that are encoded.
    for record in event["records"]:
        # Decode the payload with utf-8 to read the values from the record and enrich it
        payload = base64.b64decode(record["data"]).decode("utf-8")

        # Custom processing to enrich the payload
        try:
            json_payload = json.loads(payload)

            # Original record from VPC Flow Logs is separated by space delimiter
            flow_log_record = json_payload["message"].split(" ")

            # Ordering the values in flow log into ordered dict.
            record_dict = OrderedDict(
                {
                    "account-id": flow_log_record[1],
                    "action": flow_log_record[12],
                    "bytes": flow_log_record[9],
                    "dstaddr": flow_log_record[4],
                    "dstport": flow_log_record[6],
                    "end": flow_log_record[11],
                    "interface-id": flow_log_record[2],
                    "log-status": flow_log_record[13],
                    "packets": flow_log_record[8],
                    "protocol": flow_log_record[7],
                    "srcaddr": flow_log_record[3],
                    "srcport": flow_log_record[5],
                    "start": flow_log_record[10],
                    "version": flow_log_record[0],
                }
            )

            # Finally modify the payload with enriched record
            payload = json.dumps(record_dict) + "\n"
        except Exception as ex:
            print("Could not process record, Exception: ", ex)
            output_record = {
                "recordId": record["recordId"],
                "result": "ProcessingFailed",
                "data": base64.b64encode(payload.encode("utf-8")).decode("utf-8"),
            }
        else:
            # Assign the enriched record to the output_record for Kinesis to process it further
            output_record = {
                "recordId": record["recordId"],
                "result": "Ok",
                "data": base64.b64encode(payload.encode("utf-8")).decode("utf-8"),
            }

        # Appending the records to the output list for ingesting into destination.
        output.append(output_record)

    print("Successfully processed {} records.".format(len(event["records"])))

    return {"records": output}
