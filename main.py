'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  if n < 2 :
    return False;
  if n == 2 :
    return True;
  for i in range(2, int((n / 2)+1)) :
    if n % i == 0 :
      return False;
  return True;
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  produs = 1
  for x in lst :
    produs = produs * x
  return produs;
  
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while x != y :
    if x > y :
      x = x - y
    elif x < y :
      y = y - x
  return x;

  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  while y :
    r = x % y
    x = y
    y = r
  return x;
  
  
def main():
  while True :
    print('1. Primalitatea unui număr')
    print('2. Produsul numerelor dintr-o listă')
    print('3. CMMDC al două numere folosind scăderi repetate')
    print('4. CMMDC al două numere folosind împărțiri repetate')
    print('x. Încheie programul')
    optiune = input('Alege opțiunea: ')
    if optiune == '1' :
      n = int(input('Dați numărul:'))
      if is_prime(n) == True :
        print(f'Numărul {n} este prim.')
      else :
        print(f'Numărul {n} nu este prim.')
    elif optiune == '2' :
      numere_str = input('Dați numerele separate printr-un spațiu: ')
      numere_str_lst = numere_str.split(' ')
      numere_int_lst = []
      for nr_str in numere_str_lst :
        numere_int_lst.append(int(nr_str))
      produs = get_product(numere_int_lst)
      print(f'Produsul numerelor din listă este {produs}.')
    elif optiune == '3' :
      x = int(input('Dați primul număr: '))
      y = int(input('Dați al doilea număr: '))
      cmmdc = get_cmmdc_v1(x, y)
      print(f'Cel mai mare divizor comun al celor două numere este {cmmdc}')
    elif optiune == '4' :
      x = int(input('Dați primul număr: '))
      y = int(input('Dați al doilea număr: '))
      print(f'Cel mai mare divizor comun al celor două numere este {cmmdc}')
    elif optiune == 'x' :
      break
    else :
      print('Opțiune invalidă!')


if __name__ == '__main__':
  main()
