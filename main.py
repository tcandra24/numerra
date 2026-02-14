from utilities.input_handler import input_menu, loop_validation_input
from core.operations import execute_operation
from core.errors import CalculatorError
from core.history import History
from enums.menu import Menu
        
def main():
    histories = History()

    while True:
        try:
            print ("""
Choose Menu:
    1. Penjumlahan
    2. Pengurangan
    3. Perkalian
    4. Pembagian
    5. History
    6. Keluar
            """)
            menu = input_menu()

            if menu == Menu.EXIT: 
                print("Terima Kasih!!")
                break

            if menu == Menu.HISTORY:
                histories.show()
                continue
            
            value_1 = loop_validation_input("Masukan Angka Pertama : ")
            value_2 = loop_validation_input("Masukan Angka Kedua : ")

            result = execute_operation(menu, value_1, value_2, histories)
            print(f"Hasilnya yaitu : {result}")
        except CalculatorError as e:
            print(f"Error : {e}")
        

if __name__ == "__main__":
    main()
    

