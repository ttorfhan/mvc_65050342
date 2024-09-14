#ตรวจสอบการป้อนข้อมูล
def checkInput(cow_id: str, cow_color: str, cow_age: str) -> bool:
    """Check if the input is valid or not."""

    if not cow_id.isdigit() or len(cow_id) != 8 or cow_id[0] == '0': #เป็นตัวเลข8หลักและไม่เริ่มต้นด้วย0
        print("Cow ID must be an 8-digit number without leading zero.")
        return False

    if cow_color not in {'brown', 'white'}: #เป็น brown หรือ white
        print("Cow Color must be either 'brown' or 'white'.")
        return False

    parts = cow_age.split('.') #เป็นปี.เดือน
    if len(parts) != 2 or not parts[0].isdigit() or not parts[1].isdigit() or len(parts[0]) > 3 or len(parts[1]) > 2:
        print("Cow Age must be in the format 'year.month'.")
        return False

    return True

