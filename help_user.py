import discord
import math

def ad(phrase):
  title = '**'
  for first in range(0,math.floor((36-len(phrase))/2) if isinstance(len(phrase)/2, float) else (36-len(phrase))/2):
    title+='-'
  title+=phrase
  for last in range(0,math.ceil((36-len(phrase))/2) if isinstance(len(phrase)/2, float) else (36-len(phrase))/2):
    title+='-'
  title+='**'
  return title

def helper(color):
  print("'Help' command initiated")
  help_page = discord.Embed(title='Help Page', description ='\n',color = discord.Color.blue())
  help_page.add_field(name=ad("Basic Commands"),value='Every day commands',inline=True)
  help_page.add_field(name='ping', value = 'Returns bot-command latency', inline=False)
  help_page.add_field(name='hello', value = 'Sends a greeting', inline=False)
  help_page.add_field(name='about', value = 'Sends information regarding the bot', inline=False)
  help_page.add_field(name='man', value = 'Sends syntax of a specified command', inline=False)
  help_page.add_field(name='hiatus', value = 'Sends info. about bot\'s status', inline=False)
  help_page.add_field(name=ad("Text Altering"),value='Commands that change text format',inline=True)
  help_page.add_field(name='custom', value = 'Sends user-inputted text back', inline=False)
  help_page.add_field(name='announce', value = 'Sends user-inputted data in embedded form', inline=False)
  help_page.add_field(name='reverse', value = 'Sends user-inputted data backwards', inline=False)
  help_page.add_field(name='caesar', value = 'Sends user-inputted data encoded in a Caesar cipher with a shift of the user\'s choosing', inline=False)
  help_page.add_field(name=ad("Administrator commands"), value='Commands that required administrator permissions', inline=True)
  help_page.add_field(name="spam", value="Spams a word the number of times and intervals the user wants | Warning: This command will prompt the user to answer 'Yes' or 'No' due to the latency delay it causes.", inline = False)
  help_page.add_field(name="disable", value="Will disable other administrator commands", inline  = False)
  help_page.add_field(name="enable",value="Will enable any disabled administrator command", inline = False)
  help_page.add_field(name=ad("Hypixel Commands"), value = 'Commands used with Hypixel API', inline = True)
  help_page.add_field(name="Note", value = "You must use the command '>hypixel' and specify the second parameter using these 'sub' commands", inline = False)
  help_page.add_field(name="stats", value = "Sends the stats of the specified player. The name of the player must be officially registered on the Minecraft System", inline = False)
  help_page.add_field(name="links", value = "Sends the links used in the development of this command | Currently not present", inline = False)
  
  return help_page