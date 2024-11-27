from database import users
from atm_service import check,update,change,transfer,show_cards,change_percent,check_admin,superior,new_card
from database import users_card,users_info,atms_info,admin
import json
print('Welcome ATM')
while True:
    choise = int(input('1.User panel\n2.Admin panel\n0.Exit\n'))
    if choise == 1:
        card_number = input('Enter card number: ')
        card_pass = int(input('Enter card password: '))
        if check(card_number,card_pass):
            while True:
                select = int(input('1.Withdrav\n2.Card pin-kod\n3.Show card\n4.Transfer\n0.Exit\n'))
                if select == 1:
                    pul_yechish = float(input('Qancha miqdorda pul yechmoqchisiz: '))
                    if card_number[0] == '8':
                        protsent =  atms_info.get('uzcard').get('percent')
                    elif card_number[0] == '9':
                        protsent = atms_info.get('humo').get('percent')
                    elif card_number[0] == '4':
                        protsent = atms_info.get('visa').get('percent')
                    elif card_number[0] == '5':
                        protsent = atms_info.get('master_card').get('percent')
                    card_balance = users_card.get(card_number).get('balance')
                    card_value = users_card.get(card_number)
                    percent = pul_yechish * protsent / 100 + pul_yechish
                    if percent <= card_balance:
                        card_balance -= percent
                        card_value['balance'] = card_balance
                        print(users_card,'users_card')
                        update()
                        print(f"Sizning balansingiz:{card_balance}\nKomissiyasi bilan:{percent}")
                    else:
                        print('Balansingizda mablag yetarli emas!')
                elif select == 2:
                    old_parol = int(input('Hozirgi parolni kiriting: '))
                    if old_parol == card_pass:
                        change(card_number)
                        update()

                elif select == 3:
                    show_card = users_card.get(card_number)
                    users_id = str(users_card.get(card_number).get('user_id'))
                    print(f"Balansingiz: {show_card.get('balance')} {users_info.get(users_id).get('name')}")
                elif select == 4:
                    transfer(card_number)
                elif select == 0:
                    with open(file='cards.json',mode='w') as file:
                        json.dump(users_card,file,indent=4)
                    with open(file='atms.json',mode='w') as atm_file:
                        json.dump(atms_info,atm_file,indent=4)
                    with open(file='users.json',mode='w') as users_file:
                        json.dump(users_info,users_file,indent=4)
                    break
    elif choise == 2:
        admin_check = input('Enter admin id: ')
        admin_pass = int(input('Enter pass: '))
        checked = check_admin(admin_check,admin_pass)
        if checked[0]:
            superior(admin_pass=admin_pass,admins=admin_check)
        while checked[1]:
            admin_select= int(input('1.Show kard\n2.Change percent\n3.Delate card\n4.New card\n5.New admin\n0.Exit\n'))
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
                new_superior = bool(input('Admindan ustunroqmi True or False: '))
                if new_superior == 'False':
                    admin[new_admin_id] = {'name':new_admin_name,'code':new_admin_code, 'superior':False}
                elif new_superior == 'True':
                    admin[new_admin_id] = {'name':new_admin_name,'code':new_admin_code, 'superior':True}
                update()
                if admin.get(new_admin_id) is not None:
                    print('Yengi admin muvaffaqiyatli qoshildi✅✅✅')
            elif admin_select == 0:
                update()
                break
    elif choise == 0:
        update()
        break
