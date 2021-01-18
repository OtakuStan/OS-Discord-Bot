rules = {
            "Rule01": "Stay Respectful!!",
            "Rule02": "No Spam, neither in text channels nor in voice channels.",
            "Rule03": "No Abusing/Trash Talking (Aliases like frick, BC, MC are allowed).",
            "Rule04": "No impersonation.",
            "Rule05": "No politics or religious talks in chat.",
            "Rule06": "No Racism (this includes offensive memes that have an overall negative connotation, including the n word)",
            "Rule07": "Don't yell into your mic or be obnoxious while using the VC channels during events.",
            "Rule08": "Requesting members to avoid regional language in the group because most of the people wouldn't  know your language.",
            "Rule09": "Discussing newly released episode or any chapter from manga is allowed only in  #🤫︱spoiler-chat",
            "Rule10": "No NSFW",
            "Rule11": "No NSFW nicknames",
            "Rule12": "Please try not to be mean to other humans and bots.",
            "Rule13": "Must follow all the Discord's Terms of Service (Discord TOS - https://discord.com/terms)",
        }

def get_rule_index(index):
    keys = [*rules.keys()]
    return keys[index]

def get_rule_value(index):
    values = [*rules.values()]
    return values[index]