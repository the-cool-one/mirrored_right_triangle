def draw_mirrored_triangle(n):
    for i in range(1, n + 1):
        
        print(" " * (n - i) + "*" * i)


draw_mirrored_triangle(5)
