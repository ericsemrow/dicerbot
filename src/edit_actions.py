import discord, os, json
from discord.ext import commands
from replit import db, database
from src.repositories.rolls_repository import RollsRepository



class EditActions(commands.Cog):
  
  @commands.command()
  async def invite(self, ctx):
    """Get the invite link"""
    await ctx.sent( "https://discord.com/api/oauth2/authorize?client_id=959851494763528202&permissions=76864&scope=bot" )

  @commands.command()
  async def zimport(self, ctx, *, arg):
    """Import/overwrite entire json struct"""
    try:
      repo = RollsRepository()
      repo.store_data_for_user( arg, ctx.author.id )
      await ctx.send("Import Successful")
    except Exception as e:
      await ctx.send("There was an issue importing your json")
      raise e


  @commands.command()
  async def zexport(self, ctx):
    """Import/overwrite entire json struct"""
    try:
      repo = RollsRepository()
      jsonArg = repo.get_override_for_user(ctx.author.id)
      
      await ctx.send(json.dumps(jsonArg, indent = 4, sort_keys=True))
    except Exception as e:
      await ctx.send("There was an issue exporting your json")
      raise e

      
  @commands.command()
  async def zadd(self, ctx, *args):
    """Import/overwrite a single action"""
    pass

  @commands.command()
  async def zdelete(self, ctx, *args):
    """Remove an action"""
    pass

  @commands.command()
  async def zsample(self, ctx):
    """Here's a sample json for you to build on"""
    pass

    json = """{
    	"vars": {
    		"prof": 2,
    		"str": 1,
    		"spell": 2,
    		"brain": 0
    	},
    	"rolls": {
    		"a": {
    			"firebolt": {
    				"title": "<name> casts firebolt",
    				"roll": "3d6+prof+brain",
    				"damage": "1d10",
    				"description": "A bolt of fire"
    			}
    		},
    		"c": {
    			"athletics": {
    				"title": "<name> makes an athletics check",
    				"roll": "3d6+str"
    			},
    			"arcana": {
    				"title": "<name> makes an arcana check",
    				"roll": "3d6+brain"
    			}
    		}
    	}
    }
    """
    await ctx.send(json)
