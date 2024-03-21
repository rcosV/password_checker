import requests
import hashlib
import sys


# Function to fetch data from pwnedpasswords API
def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    # If the response status code is not 200 (OK), raise an error
    if res.status_code != 200:
        raise RuntimeError(
            f"Error fetching: {res.status_code}, check the API and try again"
        )
    return res


# Function to get the count of how many times a password has been leaked
def get_password_leaks_count(hashes, hash_to_check):
    # Split the API response and count occurrences of the password
    hashes = (line.split(":") for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


# Function to check if a password has been pwned
def pwned_api_check(password):
    # Check password if it exists in API response
    # Convert password to SHA-1 hash
    sha1password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


# Main function to check a list of passwords
def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{password} was found {count} times... you should probably change your password"
            )
        else:
            print(f"{password} was not found. Carry on!")
    return "Done!"


# Entry point of the script
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
