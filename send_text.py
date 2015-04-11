from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC1c0fbc234b7dd33d27ec3043fa6c5012"
auth_token  = "952c92647a971726f250b95912460a58"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hi malisha!",
    to="+13129736367",    # Replace with your phone number
    from_="+12013971196") # Replace with your Twilio number
print message.sid
