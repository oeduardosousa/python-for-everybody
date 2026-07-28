# Email Analyzer

has_number = False

# Get the email from the user
email = input("Enter your email: \n").strip()

# Get the length of the email, user, domain, and provider
len_email = len(email)
user_pos = email.find("@")
user = email[:user_pos]
len_user = len(user)

domain_pos = email.find(".", user_pos)
domain = email[user_pos + 1:]
len_domain = len(domain)

provider_pos = domain.find(".", 0, domain_pos)
provider = domain[:provider_pos]
len_provider = len(provider)

# Check if the email contains a number
for char in email:
    if char.isdigit():
        has_number = True
        break

# Print the results
print(f"Your email is: {email}")
print(f"Your email has {len_email} characters.")
print(f"Your email in uppercase: {email.upper()}")
print(f"Your email in lowercase: {email.lower()}\n")

print(f"Your user is: {user}")
print(f"Your user has {len_user} characters.\n")

print(f"Your domain is: {domain}")
print(f"Your domain has {len_domain} characters. \n")

print(f"Your provider is: {provider.capitalize()}")
print(f"Your provider has {len_provider} characters. \n")

print(f"Your email contains a number: {has_number}")