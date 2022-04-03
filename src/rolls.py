import discord, d20, os, json
from discord.ext import commands
from replit import db, database
from src.repositories.rolls_repository import RollsRepository



class Rolls(commands.Cog):
  
  @commands.command(aliases=['r'])
  async def roll(self, ctx, *args):
    args = list(args)
    category = args.pop(0)
    action = args.pop(0)
    
    repo = RollsRepository()
    roll = repo.get_roll_for_user(ctx.author.id, category, action)
    
    title = roll["title"].replace("<name>", ctx.author.display_name) if roll.get("title") else ""
    description = roll["description"] if roll.get("description") else ""
    attack = roll["roll"] if roll.get("roll") else False
    damage = roll["damage"] if roll.get("damage") else False

    embed = discord.Embed(title=title,description=description)

    if attack:
      embed.add_field(name="Roll", value=str(d20.roll(attack)))
    if damage:
      embed.add_field(name="Damage", value=str(d20.roll(damage)))

    await ctx.send(embed=embed)