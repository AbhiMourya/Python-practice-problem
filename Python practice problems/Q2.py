def hide(cc_num):
    if len(str(cc_num))==16:
        return str(cc_num)[-4:]
    else:
       return "Enter a valid card number."

print(hide(2453475434376874))
print(hide(12345678987654))
