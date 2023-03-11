import random
import pygame
import time

width = 1000
height = 1000
numbers = []
for y in range(height):
    numbers.append([])
    for i in range(y):
        numbers[y].append(1)
    for z in range(height - y):
        numbers[y].append(0)
for b in range(len(numbers)):
        random.shuffle(numbers[b])  
random.shuffle(numbers)
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SORTBOOLS")
for k in range(len(numbers)):
        for u in range(len(numbers[k])):
            if numbers[k][u] == 1:
                pygame.draw.rect(screen, (255,255,255), (u, k, 1, 1))
pygame.display.update()
time.sleep(5)
list_number = []
for f in range(len(numbers)):
    list_number_int = 0
    for p in range(len(numbers[f])):
        if numbers[f][p] == 1:
            list_number_int = list_number_int + 1
    list_number.append(list_number_int)
phase1 = True
phase2 = False
phase3 = False
count1 = 0
count2 = 0
FS = True
while True:
    count1 = 0
    count2 = 0
    if phase1 == True:
        for n in range(len(numbers)):
            for m in range(len(numbers[n])-1):
                if numbers[n][m] < numbers[n][m+1]:
                    x = numbers[n][m]
                    y = numbers[n][m+1]
                    numbers[n][m] = y
                    numbers[n][m+1] = x
                    count1 = count1 + 1         
    elif phase2 == True:
        FS = False
        for g in range(len(numbers) - 1):
            if list_number[g] < list_number[g+1]:
                x = list_number[g]
                y = list_number[g+1]
                list_number[g+1] = x
                list_number[g] = y

                x = numbers[g]
                y = numbers[g+1]
                numbers[g+1] = x
                numbers[g] = y
                count2 = count2 + 1
    elif phase3 == True:
        screen.fill((0,0,0))
        for k in range(len(numbers)):
            for u in range(len(numbers[k])):
                if numbers[k][u] == 1:
                    pygame.draw.rect(screen, (0,255,0), (u, k, 1, 1))
            pygame.display.update()
        time.sleep(3)
        raise SystemExit
    
    if count1 == 0:
        phase1 = False
        phase2 = True
    if count2 == 0 and FS == False:
        phase2 = False
        phase3 = True

    screen.fill((0,0,0))
    for k in range(len(numbers)):
        for u in range(len(numbers[k])):
            if numbers[k][u] == 1:
                pygame.draw.rect(screen, (255,255,255), (u, k, 1, 1))
    pygame.display.update()
    time.sleep(0.001)