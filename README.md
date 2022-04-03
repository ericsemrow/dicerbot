**Invite Link:** https://discord.com/api/oauth2/authorize?client_id=959851494763528202&permissions=76864&scope=bot


Json structure is as follows:
```
{
    "rolls": {  // Any rolls you want to make. Attacks, saves, checks, etc
        "a": {  // Category. By default a (attack), c (check), s (save)
            "firebolt": {  // Name of attack
                "damage": "1d10",  // The second roll made
                "description": "A bolt of fire", // Your desc
                "roll": "3d6+prof+cha",  // The first roll made
                "title": "<name> casts firebolt"  // A name for the embed
            }
        }
    },
    "vars": {  // These will get substituted in for on dice strings
        "dex": 1,
        "prof": 2
    }
}
```

The entire default json string can be found here:
https://github.com/ericsemrow/dicerbot/blob/main/src/data/base_data.json

You can override anything. Use a beautifier such as https://codebeautify.org/jsonminifier to make it easier on yourself. Try not to override more than needed else you'll run into the discord message limit.

## Commands

Bot prefix: `#`

`#zsample`: Exports a sample json string to get you started

`#zexport`: Exports your current override json

`#zimport <override json>`: Imports a new override string. Warning - this will overwrite your previous string.

`#r <category> <action> <optional: your init name> <optional: enemy init name>`: Rolls an attack/roll/save

#### Not yet implemented
`#zadd <category> <action json>`: Merges a roll into your override json

`#zdelete <category> <action key>`: Deletes a roll from your override json