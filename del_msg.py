import pyperclip
a = 0
num = 1
msg =['Hello! While reviewing your bot, I found the following issues:']
while a == 0:
        issue = input('List an Issue with the Bot. If you are done return nothing.\n')
    if issue == '':
        a = 1
    else:
        msg.append(f"> {num}. {issue}")
        num += 1
msg.append("Please ping me __one time__ once you've fixed __all__ the issues above, and I will re-review your bot. Thanks!")
msg1 = '\n'.join(msg)
pyperclip.copy(msg1)
print('The message has been copied to your clipboard!')
