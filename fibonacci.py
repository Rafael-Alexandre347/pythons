def fibonacci(n):
   a, b = 0, 1

   while a < n:
      a, b = b, a + b

   return a == n
   
numero = int(input("Informe um número: "))

if fibonacci(numero):
   print(f"O número {numero} faz parte da sequência de Fibonacci.")
else: print(f"O número {numero} não faz parte da sequência de Fibonacci.")