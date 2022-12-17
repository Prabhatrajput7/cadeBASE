from twilio.rest import Client

account_sid = "ACc49d4bb14f3391d56a70cd30b538886b"
auth_token = "9825de22cda7897220fc228dd2f2dec6"
client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_="+19896629343",
    to="+918744969547"
)
