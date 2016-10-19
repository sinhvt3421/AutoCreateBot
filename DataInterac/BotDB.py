import pymssql
import BotInfo

def GetAll():
    con =  pymssql.connect(server='orm.vn', user='thanh', password='TheNew0RM2015', database='tool.orm.vn_v4')
    cursor = con.cursor(as_dict=True)
    cursor.callproc('Bot_Monitor_GetAll')
    cursor.nextset()
    results = cursor.fetchall()
    con.commit()
    con.close()
    return results
def GetStatus():
    con =  pymssql.connect(server='orm.vn', user='thanh', password='TheNew0RM2015', database='tool.orm.vn_v4')
    cursor = con.cursor(as_dict=True)
    cursor.callproc('Bot_Monitor_GetStatus')
    cursor.nextset()
    results = cursor.fetchall()
    con.commit()
    con.close()
    return results
def Insert(bt):
    con =  pymssql.connect(server='orm.vn', user='thanh', password='TheNew0RM2015', database='tool.orm.vn_v4')
    cursor = con.cursor(as_dict=True)
    cursor.callproc('Bot_Monitor_Insert',(bt.proxyIp,bt.proxyPort,bt.profileName,bt.lastRequestDate,bt.weight,
                                          bt.isDead,bt.isOnQueue,bt.botStatus,bt.username,bt.password,bt.profileUrl,
                                          bt.profileUpdateDate,bt.profileHassSync,bt.profilePhoneNumber,bt.profileFriendCounter,
                                          bt.profileFollowingCounter))
    cursor.nexset()
    results = cursor.fetchone()
    con.commit()
    con.close()
    return results
def Update(bt):
    con =  pymssql.connect(server='orm.vn', user='thanh', password='TheNew0RM2015', database='tool.orm.vn_v4')
    cursor = con.cursor(as_dict=True)
    cursor.callproc('Bot_Monitor_Update',(bt.id,bt.proxyIp,bt.proxyPort,bt.profileName,bt.lastRequestDate,bt.weight,
                                          bt.isDead,bt.isOnQueue,bt.botStatus,bt.username,bt.password,bt.profileUrl,
                                          bt.profileUpdateDate,bt.profileHassSync,bt.profilePhoneNumber,bt.profileFriendCounter,
                                          bt.profileFollowingCounter))
    cursor.nexset()
    con.commit()
    con.close()