import pyperclip, json
datafile = './del_msg_data.json'# You may need to change the path to the data file.
with open(datafile) as json_file:
    data = json.load(json_file)
botsindata = len(data['bots'])
botsinreview = len(data['review'])
start = input(f'Welcome to the DEL Staff Messaging System!\n[1] Review a New Bot\n[2] Re-review a bot\n[3] Remove an Approved/Denied Bot\n[4] Toggle a Bot\'s Reviewal State\nCurrently you have {botsindata} Bots You\'re Reviewing. {botsinreview} of them need a re-reviewal.\nPlease type the number that corresponds to the action you want to do: ')
if start == '1':
    botid = input("\nPlease enter the bot's username for re-reviewal purposes.\nIf you would like to skip this step, don't send anything: ")
    if botid != '':
        bot_id = botid
        ownerid = input("\nPlease enter the owner's user id for re-reviewal purposes.\nIf you would like to skip this step, don't send anything: ")
    else:
        bot_id = 'Unknown'
        ownerid = ''
    if botid != '':
        with open(datafile) as json_file:
            data = json.load(json_file)
        if ownerid == '':
            ownerid = ''
            owner_id = 'Unknown'
        else:
            ownerid = int(ownerid)
            owner_id = ownerid
        temp = {"owner": ownerid, "bot": botid}
        data['bots'].append(temp)
        with open(datafile, 'w') as f:
            json.dump(data, f, indent=4)
    else:
        ownerid = ''
    a = 0
    num = 1
    review_type = input("[1] This Bot has had a Ticket for Privacy Policy Issues.\n[2] This Bot has Waited a long time for Reviewal and had an Improper Privacy Policy.\nIf you require a custom starting message, type the number of it now, otherwise send nothing: ")
    if review_type == '1':
        if ownerid == '':
            msg = ["Hello, Thanks for Fixing your Privacy Policy! While reviewing your bot, I found the following issues:"]
        else:
            msg = [f"Hello <@{ownerid}>, Thanks for Fixing your Privacy Policy! While reviewing your bot, I found the following issues:"]
    elif review_type == '2':
        if ownerid == '':
            msg = ["Hello, Thanks for fixing your Privacy Policy and for your Patience! While reviewing your bot, I found the following issues:"]
        else:
            msg = [f"Hello <@{ownerid}>, Thanks for Fixing your Privacy Policy and for your Patience! While reviewing your bot, I found the following issues:"]
    else:
        msg = ['Hello! While reviewing your bot, I found the following issues:']
    print('Start typing errors below!')
    while a == 0:
        issue = input('\n- ')
        if issue == '':
            a = 1
        else:
            if issue.endswith('.') == False:
                issue = f'{issue}.'
            msg.append(f"> {num}. {issue}")
            num += 1
    msg.append("Please ping me __one time__ once you've fixed __all__ the issues above, and I will re-review your bot. Thanks!")
    msg1 = '\n'.join(msg)
    pyperclip.copy(msg1)
    print('The message has been copied to your clipboard!')
elif start == '2':
    botlist = ["If the bot is not in this list, don't send anything."]
    ownerlist = ['Placeholder']
    botidlist = ['Placeholder']
    num = 1
    with open(datafile) as json_file:
        data = json.load(json_file)
    for x in data['bots']:
        bot = x['bot']
        botidlist.append(bot)
        botlist.append(f"{num}. {bot}")
        ownerlist.append(x['owner'])
        num += 1
    botlist.append("Please select the number that corresponds to the bot you want to re-review: ")
    bot_num = input('\n'.join(botlist))
    if bot_num == '':
        owner_mention = ''
        bot_id = None
    else:
        owner_id = ownerlist.pop(int(bot_num))
        bot_id = botidlist.pop(int(bot_num))
        owner_mention = f'<@{owner_id}>'
    a = 0
    num = 1
    msg =[f'Hello {owner_mention}! After re-reviewing your bot, I found the following issues:']
    print('Start typing errors below!')
    while a == 0:
        issue = input('\n- ')
        if issue == '':
            a = 1
        else:
            if issue.endswith('.') == False:
                issue = f'{issue}.'
            msg.append(f"> {num}. {issue}")
            num += 1
    msg.append("Please ping me __one time__ once you've fixed __all__ the issues above, and I will re-review your bot. Thanks!")
    msg1 = '\n'.join(msg)
    pyperclip.copy(msg1)
    if bot_id is not None:
        if bot_id in data['review']:
            data['review'].remove(bot_id)
            with open(datafile, 'w') as f:
                json.dump(data, f, indent=4)
    print('The message has been copied to your clipboard!')
elif start == '3':
    botlist = []
    ownerlist = ['Placeholder']
    delbotlist = ['Placeholder']
    num = 1
    with open(datafile) as json_file:
        data = json.load(json_file)
    for x in data['bots']:
        bot = x['bot']
        botlist.append(f"{num}. {bot}")
        delbotlist.append(bot)
        ownerlist.append(x['owner'])
        num += 1
    botlist.append("Please select the number that corresponds to the bot you want to remove: ")
    del_list = input('\n'.join(botlist))
    ownerid = ownerlist.pop(int(del_list))
    botuser = delbotlist.pop(int(del_list))
    for b in data['bots']:
        if ownerid == b['owner'] and botuser == b['bot']:
            data['bots'].remove(b)
        if botuser == b['bot'] and b['bot'] in data['review']:
            data['review'].remove(b['bot'])
    with open(datafile, 'w') as f:
        json.dump(data, f, indent=4)
    print('Successfully Removed the Bot from the List!')
elif start == '4':
    with open(datafile) as json_file:
        data = json.load(json_file)
    num = 1
    botlist = []
    reviewlist = []
    realbot = ['Placeholder']
    for x in data['bots']:
        bot = x['bot']
        realbot.append(bot)
        if bot in data['review']:
            reviewlist.append(f'{num}. {bot}')
        else:
            botlist.append(f'{num}. {bot}')
        num += 1
    reviewlist = '\n'.join(reviewlist)
    botlist = '\n'.join(botlist)
    bot_num = input(f'Bot\'s Under Review:\n{reviewlist}\nBot\'s Not Under Review:\n{botlist}\nPlease select the number that corresponds to the bot you want to toggle the reviewal state on: ')
    bot = realbot.pop(int(bot_num))
    for x in data['bots']:
        if bot == x['bot'] and x['bot'] in data['review']:
            data['review'].remove(x['bot'])
        elif bot == x['bot']:
            data['review'].append(bot)
    with open(datafile, 'w') as f:
        json.dump(data, f, indent=4)
    print('Successfully toggled the Bot\'s State of Review!')
else:
    print('Nope! Try again.')
