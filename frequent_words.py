import pandas

max = 0
file_log = [pandas.read_excel("file_path")]

user_id = {}
act = {}

for user in file_log.user_id:
    if user in user_id:
        user_id.count += 1
    else:
        user_id.id = user
        user_id.count = 1

for item in file_log.action:
    if item in act.action:
        act.count += 1
    else:
        act.action = item
        act.count = 1

for i in user_id:
    if i.count > (i-1).count:
        max = i.count
        top_user = i.id
    else:
        max = (i-1).count
        top_user = (i-1).id
print("Most Active User: %s" &top_user)

for j in act:
    if j.count > (j-1).count:
        max = j.count
        top_action = j.action
    else:
        max = (j-1).count
        top_action = (j-1).action
print("Most Common Action: %s" &top_action)