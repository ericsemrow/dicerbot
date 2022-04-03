import json, os
from replit import db, database

class RollsRepository():

  def store_data_for_user( self, data, user ):
    jsonArg = json.loads(data.replace( "\n", "" ))
    db[user] = jsonArg


  def get_data_for_user( self, user ):
    jsonArg = self.get_override_for_user( user )
    return deep_merge( std_json, jsonArg )

  def get_override_for_user( self, user ):
    return json.loads(database.dumps(db[str(user)]))

  def get_roll_for_user( self, user, category, roll, args = [] ):
    data = self.get_data_for_user( user )
    roll = data["rolls"][category][roll]

    if roll.get("roll"):
      for key, item in data["vars"].items():
        roll["roll"] = roll["roll"].replace(key, str(item))

    
    if roll.get("damage"):
      for key, item in data["vars"].items():
        roll["damage"] = roll["damage"].replace(key, str(item))
  
    return roll




from copy import deepcopy

def deep_merge(a: dict, b: dict) -> dict:
    result = deepcopy(a)
    for bk, bv in b.items():
        av = result.get(bk)
        if isinstance(av, dict) and isinstance(bv, dict):
            result[bk] = deep_merge(av, bv)
        else:
            result[bk] = deepcopy(bv)
    return result


filepath = os.path.join(os.path.relpath("src/data"), "base_data.json")
f = open(filepath, "r")
std_json = json.load(f)
f.close()
