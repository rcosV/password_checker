# password_checker
This Python script checks if a password has been compromised by using  the `pwnedpasswords` API.


# Password Checker

This Python script checks if a password has been compromised by using 
the `pwnedpasswords` API.

## How It Works

The script converts the password into a SHA-1 hash and then checks 
the `pwnedpasswords` API to see if it has been leaked in any data breaches.

## Usage

Run the script with the passwords you want to check as arguments:

```bash
python checkmypass.py [password1] [password2] ...


Security Note
Never use your actual password in the command line or store it in a script.
Always use a test password or a hashed version when checking.

Remember to replace `[password1] [password2] ...` with the actual passwords
you want to check, but be cautious with sensitive information.