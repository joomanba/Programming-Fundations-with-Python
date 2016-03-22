from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC3d934201b60abf33e0336e2155f1032d"
auth_token = "3c880e17a8ff518d7ab935*********"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="I'm Elon. Nice to meet you",
                                 to="+8201072704586",  # Replace with your phone number
                                 from_="+12015914234")  # Replace with your Twilio number
print message.sid

# HTTP 400 error: Permission to send an SMS has not been enabled
# for the region indicated by the 'To' number: +821072704586.
