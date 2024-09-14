from PyQt5.QtWidgets import QInputDialog
import random

def calculate_milk(cow_id: str, cow_color: str, cow_age: str) -> str:
    
    month = 30
    year = 12
    bsod = False
    if cow_color == 'white':
        lemon, ok = QInputDialog.getText(None, 'Input', 'Enter lemon amount:')
        if ok:
            if random.random() < 0.5 * (int(cow_age.split('.')[1]) / month):
                bsod = True
            else:
                return f'producing sour milk from {int(lemon)} lemons' if int(lemon) > 0 else 'milk'
    elif cow_color == 'brown':
        if random.random() < 1 * (int(cow_age.split('.')[0]) / year):
            bsod = True
        else:
            return 'chocolate milk'
    
    if bsod:
        return 'BSOD (Breast Supply Operation Down – วัวผลิตน้ํานมไม่ได้)'
    else:
        return 0

