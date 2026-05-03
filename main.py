
import dress, pants, costumes, everyday_dress, hoodie, pajamas, robes, shirts, tunics, underpants

text = ('0. Выйти\n1. Платья, сарафаны\n2. Брюки, бриджи, шорты\n3. Костюмы\n4. Повседневные платья\n5. Футболки, худи\n6.'
              ' Пижама\n7. Халаты\n8. Сорочки\n9. Туники\n10. Трусы ')
def main_fuction():
    print(text)
    n = int(input())
    if n == 0:
        return 0
    if n == 1:
        dress.get_data_dress()
        main_fuction()
    if n == 2:
        pants.get_data_pants()
        main_fuction()
    if n == 3:
        costumes.get_data_costumes()
        main_fuction()
    if n == 4:
        everyday_dress.get_data_everyday_dress()
        main_fuction()
    if n == 5:
        hoodie.get_data_hoodie()
        main_fuction()
    if n == 6:
        pajamas.get_data_pajamas()
        main_fuction()
    if n == 7:
        robes.get_data_robes()
        main_fuction()
    if n == 8:
        shirts.get_data_shirts()
        main_fuction()
    if n == 9:
        tunics.get_data_tunics()
        main_fuction()
    if n == 10:
        underpants.get_data_underpants()
        main_fuction()

main_fuction()

