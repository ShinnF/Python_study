def check_lower(str_engsentenses):
    if str_engsentenses == str_engsentenses.lower():
        return True
    return False


print(check_lower('down down down') == True)
print(check_lower('There were doors all round the hall, but they were all locked') == False)