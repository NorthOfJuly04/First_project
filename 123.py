import string

username = input("Enter username: ").strip()
birth_year = input("Enter your birth year (YYYY) or leave empty: ").strip()
password = input("Enter password: ").strip()

score = 0
total = 9  # 8 rules + 1 extra (birth year)
failed = []
strengths = []

common_passwords = [
    "123456", "password", "123456789", "12345678",
    "12345", "111111", "qwerty", "admin", "asdfgh", "P@s$w0rd"
]

replacements = {'a': '@', 's': '$', 'o': '0', 'i': '!'}

# 1️⃣ Length check
if len(password) >= 8:
    score += 1
    strengths.append("Good length (8+ characters)")
else:
    failed.append("❌ Password must be at least 8 characters long.")

# 2️⃣ Has letter
if any(c in string.ascii_letters for c in password):
    score += 1
    strengths.append("Contains at least one English letter")
else:
    failed.append("❌ Password must contain at least one English letter.")

# 3️⃣ Has special character
if any(c in "!@$" for c in password):
    score += 1
    strengths.append("Contains at least one special character (!,@,$)")
else:
    failed.append("❌ Password must contain at least one special character (!,@,$).")

# 4️⃣ Has uppercase
if any(c.isupper() for c in password):
    score += 1
    strengths.append("Contains uppercase letters")
else:
    failed.append("❌ Password must contain at least one uppercase letter.")

# 5️⃣ Not same as username
if password != username:
    score += 1
    strengths.append("Password is not identical to username")
else:
    failed.append("❌ Password cannot be the same as username.")

# 6️⃣ Not swapcase version
if password != username.swapcase():
    score += 1
    strengths.append("Password is not swapcase version of username")
else:
    failed.append("❌ Password cannot be the swapcase version of username.")

# 7️⃣ Not special-character version of username
special_version = username
for k, v in replacements.items():
    special_version = special_version.replace(k, v)
if password != special_version:
    score += 1
    strengths.append("Password is not a special-character version of username")
else:
    failed.append("❌ Password is a special-character version of username (like s→$, a→@, etc.)")

# 8️⃣ Not a common password
if password not in common_passwords:
    score += 1
    strengths.append("Not a common or weak password")
else:
    failed.append("❌ Password is too common or weak.")

# 9️⃣ Extra: Does not contain birth year
if birth_year:
    if birth_year not in password:
        score += 1
        strengths.append("Does not contain your birth year")
    else:
        failed.append("❌ Password contains your birth year.")
else:
    # If user didn’t give year, count as neutral (passed)
    score += 1

# 💯 Final result
print("\n✅ Filter checks complete.\n")
print(f"🔐 Final Score: {score} out of {total}")

if score <= 3:
    level = "Very Weak"
elif score <= 6:
    level = "Medium"
else:
    level = "Strong"

print(f"🔒 Security Level: {level}\n")

# 💪 Strengths and fails
if strengths:
    print("💪 Strengths:")
    for s in strengths:
        print("-", s)

if failed:
    print("\n⚠️ Failed Checks:")
    for f in failed:
        print(f)
else:
    print("\n🎉 Congratulations! Your password passed all security checks.")
    print("I`m Amir")