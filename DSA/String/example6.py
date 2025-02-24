# Python – Convert Snake case to Pascal case

string= "aabbb_cc_dd_eee"
res= string.replace("_"," ").title().replace(" ", "")
print(res)