**Invite Link:** https://discord.com/api/oauth2/authorize?client_id=959851494763528202&permissions=76864&scope=bot


Json structure is as follows:
```{
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
}```

