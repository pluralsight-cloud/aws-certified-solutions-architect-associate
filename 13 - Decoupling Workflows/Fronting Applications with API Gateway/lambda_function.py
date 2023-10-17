import json
import http.client


def lambda_handler(event, context):
    # Get a random quote from the internet
    conn = http.client.HTTPSConnection("zenquotes.io")
    conn.request("GET", "/api/random")
    response = conn.getresponse()

    if response.status == 200:
        data = json.loads(response.read().decode())
        quote = data[0]["q"]
        author = data[0]["a"]

        # Return the quote in the response
        return {"statusCode": 200, "body": f"{quote} -- {author}"}
    else:
        # Handle any potential errors
        return {"statusCode": response.status, "body": "Failed to fetch a quote."}
