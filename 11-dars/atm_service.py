from database import users_card,users_info,atms_info,admin
import json
import random


def check(number,password):
    for i in users_card:
        if i == number:
            if users_card.get(i).get('code') == password:
                return True
            else:
                return False
        else:
            return False


def update():
    with open(file='cards.json',mode='w') as file:
        json.dump(users_card,file,indent=4)
    with open(file='atms.json',mode='w') as atm_file:
        json.dump(atms_info,atm_file,indent=4)
    with open(file='users.json',mode='w') as users_file:
        json.dump(users_info,users_file,indent=4)
    with open(file='admins.json',mode='w') as admins_file:
        json.dump(admin,admins_file,indent=4)
def change(card_number):
        change_pass = input('Yangi pin-kodni kiriting: ')
        repeat_pass = input('Pin kodni qaytadan kiriting: ')
        if change_pass == repeat_pass:
            if len(change_pass) > 4 or len(change_pass) <4:
                print('Pin kodingiz 4 ta sondan iborat bolish kerak')
            elif len(change_pass) == 4:
                card_code = users_card.get(card_number)
                card_code['code'] = int(change_pass)
                if card_code['code'] == int(change_pass):
                    print('Pin-kod muvaffaqiyatli ozgartirildi✅')
                else:
                    print('Error')
            else:
                print('Parolingizni uzunligi 4-ta raqamdan iborat blishi kerak!')
        else:
            print('Parol bir biriga togri kelmadi!🤷‍♂️')
def transfer(card_number):
    transfer_card = input('Qaysi kartaga pul otkazmoqchisiz: ')
    if users_card.get(transfer_card) is not None:
        pul_miqdori = int(input('Pul miqdorini kiriting: '))
        pin_kod = int(input('Pinkodingizni kiriting: '))
        if pin_kod == users_card.get(card_number).get('code'):
            balance = users_card.get(card_number).get('balance')
            transfer_protsent = pul_miqdori * 2 /  100 + pul_miqdori
            once_card = users_card.get(card_number)
            second_card = users_card.get(transfer_card)
            if transfer_protsent <= balance:
                once_card['balance'] -= transfer_protsent
                second_card['balance'] += pul_miqdori
                update()
                print('✅✅✅')
            else:
                print('Balansingizda yetarli mablag yoq🤷‍♂️')

def show_cards(selected:int) -> dict:
    with open(file='cards.json',mode='r') as cards:
        users_card = json.load(cards)
    with open(file='users.json',mode='r') as users:
        users_info = json.load(users)
    with open(file='atms.json',mode='r') as amts:
        atms_info  = json.load(amts)
    if selected == 1:
        for cards,card_value in users_card.items():
            print(cards,card_value)
    elif selected == 2:
        for user,user_value in users_info.items():
            print(user,user_value)
    elif selected == 3:
        for atm,atm_value in atms_info.items():
            print(atm,atm_value)

def change_percent():
    for key,value in atms_info.items():
        print(f'{key}: {value}')
    choose = input('Qaysi kartaning protsentini ozgartimoqchisiz: ')
    if atms_info.get(choose) is not None:
        get_atm = atms_info.get(choose)
        change_percent = float(input('Yangi protsentni kiriting: '))
        get_atm['percent'] = change_percent
        update()
        if get_atm['percent'] == change_percent:
            print('Protsent muvaffaqiyatli ozgartirildi✅✅✅')
        else:
            print('Protsent ozgartirishda xato🤷‍♂️')
    else:
        print('Bunday karta mavjud emas🤷‍♂️')


def check_admin(admin_id,admin_pass):
    for id in admin:
        if id == admin_id:
            if admin.get(id).get('code') == admin_pass:
                if admin.get(id).get('superior') == True:
                    return True,False
                elif admin.get(id).get('superior') == False:
                    return False,True
    return False,False


def superior(admin_pass,admins):
    while True:
        admin_select= int(input('1.Show kard\n2.Change percent\n3.Delate card\n4.New card\n5.New admin\n6.Delate admin\n0.Exit\n'))
        if admin_select == 1:
            while True:
                select_show = int(input('1.Show cards\n2.Show users\n3.Show atms\n0.Exit\n'))
                if select_show == 0:
                    update()
                    break
                show_cards(select_show)
        elif admin_select == 2:
            change_percent()
        elif admin_select == 3:
            check_pass = int(input('Admin parol kiriting: '))
            if check_pass == admin_pass:
                for key,value in users_card.items():
                    print(key,value)
                delate_card = int(input('Qaysi cardni ochirmoqchisiz User Id kiriting: '))
                for z in users_card:
                    users_id = users_card.get(z).get('user_id')
                    if users_id == delate_card:
                        users_card.pop(z)
                        update()
                        print('Carta muvaffaqiyatli ochirildi✅✅✅')
                        break
            else:
                print('Admin parol xato❌')
        elif admin_select == 4:
            print('Yengi carta raqam turini tanlang')
            new_card_num = int(input('1.Uzcard\n2.Humo\n3.Visa\n4.Master Card\n'))
            pinkod = int(input('Carta pin-kodini kiriting: '))
            balans = int(input('Karta balansini kiriting: '))
            new_user_name = input('User ismini kiriting: ')
            user_age  = int(input('Userning yoshini kiriting: '))
            new_card(new_card_num,code=pinkod,balance=balans,user_id=len(users_info)+1,user_name=new_user_name,user_age=user_age)
        elif admin_select == 5:
            new_admin_id = input('Yengi admin id-sini kiriting: ')
            new_admin_code = int(input('Yengi admin code: '))
            new_admin_name = input('New admin name: ')
            new_superior = input('Admindan ustunroqmi True or False: ')
            if new_superior == 'False':
                admin[new_admin_id] = {'name':new_admin_name,'code':new_admin_code, 'superior':False}
            elif new_superior == 'True':
                admin[new_admin_id] = {'name':new_admin_name,'code':new_admin_code, 'superior':True}
            update()
            if admin.get(new_admin_id) is not None:
                print('Yengi admin muvaffaqiyatli qoshildi✅✅✅')
        elif admin_select == 6:
            for key,value in admin.items():
                if key == admins:
                    continue
                print(key,value)
            del_admin = int(input('Admin id sini kiriting: '))
            if admin.get(del_admin) is not None:
                admin.pop(del_admin)
                print('Admin muvaffaqiyatli ochirildi✅✅✅')
            else:
                print('Bu admin Id mavjud emas')
        elif admin_select == 0:
            update()
            break

def new_card(num,code,user_id,balance,user_name,user_age):
    random_number = random.randint(111111111111111,999999999999999)
    users_info[len(users_info)+1] = {'name':user_name,"age":user_age}
    if num == 1:
        users_card[f'8{str(random_number)}'] = {'code':code,"balance":balance,'user_id':user_id}
        print('Carta muvaffaqiyatli yaratildi✅')
    elif num == 2:
        users_card[f'9{str(random_number)}'] = {'code':code,"balance":balance,'user_id':user_id}
        print('Carta muvaffaqiyatli yaratildi✅')
    elif num == 3:
        users_card[f'4{str(random_number)}'] = {'code':code,"balance":balance,'user_id':user_id}
        print('Carta muvaffaqiyatli yaratildi✅')
    elif num == 4:
        users_card[f'5{str(random_number)}'] = {'code':code,"balance":balance,'user_id':user_id}
        print('Carta muvaffaqiyatli yaratildi✅')
    else:
        print('Notogri amal')
    update()