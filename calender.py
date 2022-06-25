'''from replit import db

#Calender array 
#each item in array is a remind object
#"Title" : ExampleTitle
#"Due Date" :
#"Class" :
#"Link" :


remind_channel_id = ""# make a channel and get the channel_id to make periodic announcements
@client.command(name = 'calender')
async def calender(ctx, para=None):
  try:
    x =len(db["calender"][0]['title'])
  except:
    db["calender"] = []
    print("default")
  channel = ctx.channel
  def check(m):
      return m.channel == channel and m.author == ctx.author
  if para == 'add':
    await ctx.send("Assignment name:")
    try: #collects title, duedate, and class(Eng, WHAP, etc.)
      title = await client.wait_for('message', check=check, timeout = 20.00)
      await ctx.send("When is it due? (MM/DD/YYYY)")
      duedate = await client.wait_for('message', check=check, timeout = 20.00)
      await ctx.send("What class is this for?")
      classs = await client.wait_for('message', check=check, timeout = 20.00)
      print(title.content + " " + duedate.content + " " + classs.content)
      try:
        m, d, y = map(int, duedate.content.split('/'))
        if y<2020 or m>12 or m<1 or d>31 or d<1:
          raise Exception()
          t =100*m+ d
          wrongdates = [229,230,231,431,631,931,1131]
          if y%4==0:
            wrongdates.pop(0)
          for i in wrongdates:
            if i==t:
              raise Exception()
      except:
        await ctx.send("Invalid Date!")
        return
      duedatenum = 10000*y + 100*m+ d
      addition = {
        "title": title.content,
        "dueDate" : duedate.content,
        "class" : classs.content,
        "dueDateNum" : duedatenum,
        "inputter": ctx.author.name+ "#" + str(ctx.author.discriminator)
      }
      if len(db['calender']) ==0:
        db['calender'].append(addition)
        print("0")
      else:
        for date in db['calender']:
          print (db['calender'].index(date))
          if date['dueDateNum'] >= addition['dueDateNum']:
            print("lessgo")
            index = db['calender'].index(date)
            db['calender'].insert(index,addition)
      print(db['calender'].index(addition))
      await ctx.send("Assignment added successfully.")
      
    except asyncio.TimeoutError:
      await ctx.send("Too Slow!")
      return
    except ValueError:
      db['calender'].append(addition)
      await ctx.send("Assignment added successfully.")
    except:
      await ctx.send("Error")
      return
  elif para == "remove":
    await ctx.send("What number assignment do you want to remove? (" + str(0) + " to " + str(len(db["calender"])-1) + ")")
    try:
      index = await client.wait_for('message', check=check, timeout = 20.00)
      index = int(index.content)
    except asyncio.TimeoutError:
      await ctx.send("Too Slow!")
    try:
      x = db['calender'][index]['title']
      db['calender'].pop(index)
      await ctx.send("Removed " +x)
    except:
      await ctx.send("Invalid Index")
  elif para == "clear":
    db['calender'] = []
  elif para == None: #not tested
    cal_embed = discord.Embed(title='Assignments', description='List of assignments',color = discord.Color.default())
    x = 0
    for item in db['calender']:
      print(item)
      cal_embed.add_field(name = str(x)+ ". " + item['title'], value = "Due: "+ item['dueDate'] + "\n Class: "+ item['class'] + "\n Inputted by: " + item['inputter'])
      x+=1
    await ctx.send(embed = cal_embed)

#yoinked code form here https://stackoverflow.com/questions/63769685/discord-py-how-to-send-a-message-everyday-at-a-specific-time
async def checkAnnouncement():
  WHEN = time()
  now = datetime.utcnow()
  if now.time() > WHEN:  # Make sure loop doesn't start after {WHEN} as then it will send immediately the first time as negative seconds will make the sleep yield instantly
    tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
    seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
    await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start 
  while True:
    now = datetime.utcnow() # You can do now() or a specific timezone if that matters, but I'll leave it with utcnow
    target_time = datetime.combine(now.date(), WHEN)  # 6:00 PM today (In UTC)
    seconds_until_target = (target_time - now).total_seconds()
    await asyncio.sleep(seconds_until_target)  # Sleep until we hit the target time
    await called_once_a_day()  # Call the helper function that sends the message
    tomorrow = datetime.combine(now.date() + timedelta(days=1), time(0))
    seconds = (tomorrow - now).total_seconds()  # Seconds until tomorrow (midnight)
    await asyncio.sleep(seconds)   # Sleep until tomorrow and then the loop will start a new iteration

client.loop.create_task(checkAnnouncement())
'''