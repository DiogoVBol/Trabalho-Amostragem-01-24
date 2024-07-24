x = int(input())


nota_100 = x//100
nota_50 = (x % 100) // 50
nota_20 = ((x % 100) % 50) // 20
nota_10 = (((x % 100) % 50) % 20) // 10
nota_5 = ((((x % 100) % 50) % 20) % 10) // 5
nota_2 = (((((x % 100) % 50) % 20) % 10) % 5) // 2
nota_1 = ((((((x % 100) % 50) % 20) % 10) % 5) % 2) // 1


print(x, f'{nota_100} nota(s) de R$ 100,00', f'{nota_50} nota(s) de R$ 50,00', f'{nota_20} nota(s) de R$ 20,00',f'{nota_10} nota(s) de R$ 10,00',f'{nota_5} nota(s) de R$ 5,00',f'{nota_2} nota(s) de R$ 2,00',f'{nota_1} nota(s) de R$ 1,00',sep = "\n")
