from id_from_username import IdFromUsername
from get_friends import GetFriends

user = IdFromUsername('4taaa')
uid = user.execute()

friends = GetFriends(uid)
statistic = friends.execute()
statistic = sorted(statistic.items(), key = lambda x:x[0])
for i in statistic:
    print( '{} => {}'.format(i[0], i[1]))

