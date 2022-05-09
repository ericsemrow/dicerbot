import json, os, argparse
from tinydb import TinyDB, Query

parser = argparse.ArgumentParser(description='Take in params')
parser.add_argument('-d', "--damage", default=0, type=str, help='Dice to add to your damage roll')
parser.add_argument('-b', "--bonus", default=0, type=str, help='Dice to add to your attack roll')

class RollsRepository():

  def __init__(self):
    self.db = TinyDB('/opt/storage/db.json')
    self.q = Query()

  def store_data_for_user( self, data, user ):
    jsonArg = json.loads(data.replace( "\n", "" ))
    self.db.upsert({'userId': user, 'payload': jsonArg}, self.q.userId == user)

  def get_data_for_user( self, user ):
    jsonArg = self.get_override_for_user( user )

    return deep_merge( std_json, jsonArg )

  def get_override_for_user( self, user ):
    results = next(iter(self.db.search(self.q.userId == user)), {"payload": {}})
    return results["payload"]

  def get_roll_for_user( self, user, category, roll, other = [] ):
    data = self.get_data_for_user( user )
    parsed = parser.parse_args(other)
    print( parsed )
    print( parsed.bonus )
    print( parsed.damage )
    roll = data["rolls"][category][roll]

    if roll.get("roll"):
      for key, item in data["vars"].items():
        roll["roll"] = roll["roll"].replace(key, str(item))

      roll["roll"] += (f'+{parsed.bonus}' if parsed.bonus else "")

    
    if roll.get("damage"):
      for key, item in data["vars"].items():
        roll["damage"] = roll["damage"].replace(key, str(item))

      roll["damage"] += (f'+{parsed.damage}' if parsed.damage else "")
  
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
