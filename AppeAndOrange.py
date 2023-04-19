def countApplesAndOranges(s, t, a, b, m, apples, n, oranges):
    apple_count = 0
    orange_count = 0
    
    for i in range(m):
        apple_position = a + apples[i]
        if apple_position >= s and apple_position <= t:
            apple_count += 1
    
    for i in range(n):
        orange_position = b + oranges[i]
        if orange_position >= s and orange_position <= t:
            orange_count += 1
            
    print(apple_count)
    print(orange_count)

# lectura de la entrada del usuario
s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
apples = list(map(int, input().split()))
oranges = list(map(int, input().split()))

# llamada a la función y salida de los resultados
countApplesAndOranges(s, t, a, b, m, apples, n, oranges)