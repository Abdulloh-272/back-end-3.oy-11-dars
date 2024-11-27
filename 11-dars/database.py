import json
def while_loop(bool=True):
    if bool != 'False':
        while bool:
            new_dict = {
                '8600111111111111':{'code':4111,"balance":5_000_000,'user_id':1},
                '9860555555554444':{'code':5544,"balance":5_000_000,'user_id':2},
                '4600822463100050':{'code':3700,"balance":5_000_000,'user_id':3},
                '5174111111111117':{'code':6011,"balance":5_000_000,'user_id':4},
}
            users ={
                '1':{'name': '1:User-Ketmon',"age":18},
                '2':{'name': '2:User-Ketmon',"age":19},
                '3':{'name': '3:User-Ketmon',"age":20},
                '4':{'name': '4:User-Ketmon',"age":22},
}
            atms = {
                'uzcard':{'name':'Kapitalbank','percent':1.5},
                'humo':{'name':'Kapitalbank','percent':1.7},
                'visa':{'name':'Kapitalbank','percent':2},
                'master_card':{'name':'Kapitalbank','percent':2.1},
}
            admins = {
                '903035':{'name':'1:Admin name','code':3530, 'superior':True},
                '890407':{'name':'2:Admin name','code':3443, 'superior':False},
                '324354':{'name':'3:Admin name','code':7457, 'superior':False},
                '213123':{'name':'4:Admin name','code':9009, 'superior':False}
            }
            with open(file='cards.json',mode='w') as file:
                json.dump(new_dict,file,indent=4)
            with open(file='atms.json',mode='w') as atm_file:
                json.dump(atms,atm_file,indent=4)
            with open(file='users.json',mode='w') as users_file:
                json.dump(users,users_file,indent=4)
            with open(file='admins.json',mode='w') as admins_file:
                json.dump(admins,admins_file,indent=4)
            with open(file='truefalse.txt',mode='w') as truefalse:
                truefalse.write('False')
                break


try:
    with open(file='truefalse.txt',mode='r') as truefalse:
        while_loop(truefalse.read())
except FileNotFoundError:
    while_loop(True)



with open(file='cards.json',mode='r') as cards:
    users_card = json.load(cards)
with open(file='users.json',mode='r') as users:
    users_info = json.load(users)
with open(file='atms.json',mode='r') as amts:
    atms_info  = json.load(amts)
with  open(file='admins.json',mode='r') as admins_file:
    admin = json.load(admins_file)

print(len(users_info))
