import discord, d20, os, json
from discord.ext import commands
from src.repositories.rolls_repository import RollsRepository



class Rolls(commands.Cog):
  
  @commands.command(aliases=['r'])
  async def roll(self, ctx, *args):
    args = list(args)
    category = args.pop(0)
    action = args.pop(0)
    other = args
    
    repo = RollsRepository()
    roll = repo.get_roll_for_user(ctx.author.id, category, action, other)
    
    title = roll["title"].replace("<name>", ctx.author.display_name) if roll.get("title") else ""
    description = roll["description"] if roll.get("description") else ""
    attack = roll["roll"] if roll.get("roll") else False
    damage = roll["damage"] if roll.get("damage") else False

    embed = discord.Embed(title=title,description=description)

    if attack:
      atk = d20.roll(attack)
      embed.add_field(name="Roll", value=str(atk))
    if damage:
      dmg = d20.roll(damage)
      embed.add_field(name="Damage", value=str(dmg))

    await ctx.send(embed=embed)

    if attack and damage:
      await ctx.send(f'`!i aoo "{args[0] if 0 <= 0 < len(args) else ctx.author.display_name}" "Custom Attack" -t "{args[1] if 0 <= 1 < len(args) else "baddie"}" -custom -attackroll {atk.total} -d {dmg.total}`')