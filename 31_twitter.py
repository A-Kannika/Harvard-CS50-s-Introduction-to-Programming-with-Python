# Day 7: Dec 20, 2023
# YouTube Link
# https://youtu.be/nLRL_NcnK-4?si=HCmer8vpjqvXFKbw
# From 10:05:00 - 10:37:30

import re

def main():
        twitter_username()

def twitter_username():
        url = input("URL: ").strip()

        # re.sub(pattern, repl, string, count=0, flags=0)
        # sub -> substitution
        # be careful with . when you use the regular expression (add \)
        # ? -> 0 or 1 of the thing before it
        # (?:...) -> non capturing group, so (?:.+) and (?:www\.) doesn't capture as a group
        # the username will be this group ([a-z0-9_]+)

        if matches := re.search(r"^(?:.+)?https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
                print(f"Username: ", matches.group(1))

if __name__ == "__main__":
        main()