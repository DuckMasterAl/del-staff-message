import pyperclip, json
datafile = '/Users/duckmasteral/Documents/GitHub/del-staff-message/del_msg_data.json'# You may need to change the path to the data file.

start = input('Welcome to the DEL Staff Messaging System!\n[1] Review a New Bot\n[2] Re-review a bot\n[3] Remove an Approved/Denied Bot\nPlease type the number that corresponds to the action you want to do: ')
if start == '1':
    botid = input("\nPlease enter the bot's username for re-reviewal purposes.\nIf you would like to skip this step, don't send anything: ")
    if botid != '':
        bot_id = botid
        ownerid = input("\nPlease enter the owners's user id for re-reviewal purposes.\nIf you would like to skip this step, don't send anything: ")
    else:
        bot_id = 'Unknown'
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
    a = 0
    num = 1
    msg =['Hello! While reviewing your bot, I found the following issues:']
    print('Start typing errors below!')
    while a == 0:
        try:
            issue = input('\n- ')
        except Traceback:
            pyperclip.copy(msg)
            print('Copied all the Bot\'s Issues to your Clipboard! Next time, you can paste them and get started again!')
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
    num = 1
    with open(datafile) as json_file:
        data = json.load(json_file)
    for x in data['bots']:
        bot = x['bot']
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
    with open(datafile, 'w') as f:
        json.dump(data, f, indent=4)
    print('Successfully Removed the Bots from the List!')
else:
    print('Nope! Try again.')
