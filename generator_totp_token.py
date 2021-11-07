import pyotp

username = "your_username"
gtoken = pyotp.random_base32(64)
data = pyotp.totp.TOTP(gtoken).provisioning_uri(username, issuer_name="MyTimeTagger")
print("gtoken", gtoken)
print("qrcode data", data)
