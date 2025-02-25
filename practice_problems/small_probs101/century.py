def century(year):
   centur = year // 100
   if year % 10 != 0:
      a = centur + 1
   else:
      a = centur
   
   str_year = str(a)
   last_two = str_year[-2:]
   last = str_year [-1]

   if last_two in ['11', '12', '13']:
      match last_two:
         case '11'|'12'|'13':
            b = 'th'
   else:
      match last:
         case '1':
            b = 'st'
         case '2':
            b = 'nd'
         case '3':
            b = 'rd'
         case _:
            b = 'th'
   a = str(a)
   return a + b

print(century(2000))
print(century(2001))
print(century(1965))
print(century(256))
print(century(5))
print(century(10103))
print(century(1052))
print(century(1127))
print(century(11201))
print(century(2354))
print(century(43))
print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True