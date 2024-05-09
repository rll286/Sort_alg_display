import random
import pygame
import keyboard
import sys

pygame.init()
screen = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 20)
clock = pygame.time.Clock()
pygame.event.set_blocked(None)

def main():
    if len(sys.argv) > 1:
        number_of_tests = int(sys.argv[1])
    else:
        number_of_tests = 1
    total_iterations_sort_1 = 0
    total_iterations_sort_2 = 0
    total_iterations_sort_3 = 0
    total_iterations_sort_4 = 0
    total_iterations_sort_b = 0
    total_iterations_sort_g = 0
    total_iterations_sort_dpb = 0
    total_iterations_sort_dpg = 0
    total_iterations_sort_m = 0
    total_iterations_sort_bogo = 0

    for _ in range(number_of_tests):
        list_to_sort = list(range(1, 100 + 1))
        random.shuffle(list_to_sort)
        iterations_sort_1 = sort_1(list_to_sort.copy())
        total_iterations_sort_1 += iterations_sort_1
        
        iterations_sort_2 = sort_2(list_to_sort.copy())
        total_iterations_sort_2 += iterations_sort_2

        iterations_sort_3 = sort_3(list_to_sort.copy())
        total_iterations_sort_3 += iterations_sort_3

        iterations_sort_4 = sort_4(list_to_sort.copy())
        total_iterations_sort_4 += iterations_sort_4
        
        iterations_sort_b = sort_b(list_to_sort.copy())
        total_iterations_sort_b += iterations_sort_b

        iterations_sort_g = sort_g(list_to_sort.copy())
        total_iterations_sort_g += iterations_sort_g

        iterations_sort_dpb = sort_dpb(list_to_sort.copy())
        total_iterations_sort_dpb += iterations_sort_dpb

        iterations_sort_dpg, list_ = sort_dpg(list_to_sort.copy())
        total_iterations_sort_dpg += iterations_sort_dpg

        iterations_sort_m = sort_m(list_to_sort.copy())
        total_iterations_sort_m += iterations_sort_m

        iterations_sort_bogo = sort_bogo(list_to_sort.copy())
        total_iterations_sort_bogo += iterations_sort_bogo
    
    average_iterations_sort_1 = total_iterations_sort_1 // number_of_tests
    average_iterations_sort_2 = total_iterations_sort_2 // number_of_tests
    average_iterations_sort_3 = total_iterations_sort_3 // number_of_tests
    average_iterations_sort_4 = total_iterations_sort_4 // number_of_tests
    average_iterations_sort_b = total_iterations_sort_b // number_of_tests
    average_iterations_sort_g = total_iterations_sort_g // number_of_tests
    average_iterations_sort_dpb = total_iterations_sort_dpb // number_of_tests
    average_iterations_sort_dpg = total_iterations_sort_dpg // number_of_tests
    average_iterations_sort_m = total_iterations_sort_m // number_of_tests
    average_iterations_sort_bogo = total_iterations_sort_bogo // number_of_tests
    
    print("Average iterations for sort_1:", average_iterations_sort_1)
    print("Average iterations for sort_2:", average_iterations_sort_2)
    print("Average iterations for sort_3:", average_iterations_sort_3)
    print("Average iterations for sort_4:", average_iterations_sort_4)
    print("Average iterations for sort_b:", average_iterations_sort_b)
    print("Average iterations for sort_g:", average_iterations_sort_g)
    print("Average iterations for sort_dpb:", average_iterations_sort_dpb)
    print("Average iterations for sort_dpg:", average_iterations_sort_dpg)
    print("Average iterations for sort_m:", average_iterations_sort_m)
    print("Average iterations for sort_bogo:", average_iterations_sort_bogo)

    while not keyboard.is_pressed('esc'):
        pygame.event.pump()
    
    pygame.quit()

def update_display(list_to_sort, fps, test_name = None):
    x = 0
    color = (255, 255, 255)

    text = font.render(test_name, True, (255, 0, 0))
    textRect = text.get_rect()
    textRect.topleft = (20, 20)
    screen.fill(color)

    if keyboard.is_pressed('space'):
        fps *= 3

    if keyboard.is_pressed('shift+space'):
        fps = 0

    for element in list_to_sort:
        pygame.draw.rect(screen, "black", (x, 0, 10, 500 - (element * 5)))

        x += 10

    screen.blit(text, textRect)
    pygame.display.flip()
    pygame.event.pump()

    clock.tick(fps)

    if keyboard.is_pressed('esc'):
        sys.exit()

def sort_1(list_to_sort):
    iterations = 0

    while not is_sorted(list_to_sort):
      #  print(iterations)
        if list_to_sort[0] > list_to_sort[1]:
            temp = list_to_sort[0]
            list_to_sort[0] = list_to_sort[1]
            list_to_sort[1] = temp

        largest_number = list_to_sort[-1]
        smallest_number = list_to_sort[0]

        for value in list_to_sort:
            if value >= largest_number:
                largest_number = value
                list_to_sort.append(list_to_sort.pop(list_to_sort.index(value)))
                
            elif value <= smallest_number:
                smallest_number = value
                list_to_sort.insert(0, list_to_sort.pop(list_to_sort.index(value)))

            for index in range(len(list_to_sort) - 1):
                if list_to_sort[index] > list_to_sort[index + 1]:
                    temp = list_to_sort[index]
                    list_to_sort[index] = list_to_sort[index + 1]
                    list_to_sort[index + 1] = temp
                
                update_display(list_to_sort, 480, 'Sort 1')

                iterations += 1

            iterations += 1
    
    return iterations

def is_sorted(list_to_sort):
    for value in range(len(list_to_sort) - 1):
        current_value = list_to_sort[value]
        next_value = list_to_sort[value + 1]
        if current_value > next_value:
            return False
    
    return True

def sort_2(list_to_sort):
    iterations = 0

    while not is_sorted(list_to_sort):
        for index in range(1, len(list_to_sort) - 1):
            value1 = list_to_sort[index - 1]
            value2 = list_to_sort[index]
            value3 = list_to_sort[index + 1]

            if value1 > value3:
                temp = value1
                value1 = value3
                value3 = temp
            
            if value1 > value2:
                temp = value1
                value1 = value2
                value2 = temp

            if value2 > value3:
                temp = value2
                value2 = value3
                value3 = temp

            list_to_sort[index - 1] = value1
            list_to_sort[index] = value2
            list_to_sort[index + 1] = value3

            update_display(list_to_sort, 240, 'Sort 2')

            iterations += 1

    return iterations

def sort_b(list_to_sort):
    iterations = 0

    while not is_sorted(list_to_sort):
        for index in range(len(list_to_sort) - 1):
            if list_to_sort[index] > list_to_sort[index + 1]:
                temp = list_to_sort[index]
                list_to_sort[index] = list_to_sort[index + 1]
                list_to_sort[index + 1] = temp

            update_display(list_to_sort, 480, 'Bubble Sort')

            iterations += 1

    return iterations

def sort_g(list_to_sort):
    iterations = 0

    while not is_sorted(list_to_sort):
        index = 0
        while index < len(list_to_sort) - 1:
            if list_to_sort[index] > list_to_sort[index + 1]:
                temp = list_to_sort[index]
                list_to_sort[index] = list_to_sort[index + 1]
                list_to_sort[index + 1] = temp

                if index != 0:
                    index -= 1
            
            else:
                index += 1

            iterations += 1

            update_display(list_to_sort, 480, "Gnome Sort")
    
    return iterations

def sort_dpb(list_to_sort):
    iterations = 0

    while not is_sorted(list_to_sort):
        small_index = 0
        large_index = -1
        while small_index < len(list_to_sort) - 1:
            if list_to_sort[small_index] > list_to_sort[small_index + 1]:
                temp = list_to_sort[small_index]
                list_to_sort[small_index] = list_to_sort[small_index + 1]
                list_to_sort[small_index + 1] = temp

            if list_to_sort[large_index] < list_to_sort[large_index - 1]:
                temp = list_to_sort[large_index]
                list_to_sort[large_index] = list_to_sort[large_index - 1]
                list_to_sort[large_index - 1] = temp

            small_index += 1
            large_index -= 1

            iterations += 1

            update_display(list_to_sort, 120, "Dual Pointer Bubble")

    return iterations

def sort_dpg(list_to_sort):
    iterations = 0

    while not is_sorted(list_to_sort):
        small_index = 0
        large_index = -1
        while small_index < len(list_to_sort) // 2 or large_index > 0 - len(list_to_sort) // 2:
            if small_index >= len(list_to_sort) - 1:
                pass
            elif list_to_sort[small_index] > list_to_sort[small_index + 1]:
                temp = list_to_sort[small_index]
                list_to_sort[small_index] = list_to_sort[small_index + 1]
                list_to_sort[small_index + 1] = temp

                if small_index != 0:
                    small_index -= 1
            else:
                small_index += 1

            if large_index <= 0 - len(list_to_sort) + 1:
                pass
            elif list_to_sort[large_index] < list_to_sort[large_index - 1]:
                temp = list_to_sort[large_index]
                list_to_sort[large_index] = list_to_sort[large_index - 1]
                list_to_sort[large_index - 1] = temp

                if large_index != -1:
                    large_index += 1
            else:
                large_index -= 1

            iterations += 1

            update_display(list_to_sort, 120, "Dual Pointer Gnome" )

    return iterations, list_to_sort

def sort_3(list_to_sort):
    iterations = 0

    while not is_sorted(list_to_sort):
        index = 0
        while index < len(list_to_sort):
            smallest_number_index = index

            for value in range(index, len(list_to_sort)):
                if list_to_sort[value] < list_to_sort[smallest_number_index]:
                    smallest_number_index = value

                iterations += 1

            if index != smallest_number_index:
                list_to_sort.insert(index, list_to_sort.pop(smallest_number_index))

            index += 1

            update_display(list_to_sort, 15, "Sort 3")

    return iterations

def sort_4(list_to_sort):
    iterations = 0

    while not is_sorted(list_to_sort):
        index = 0
        
        while index < len(list_to_sort) // 2:
            smallest_number_index = index
            largest_number = list_to_sort[index]

            for value in range(index, len(list_to_sort)):
                if list_to_sort[value] < list_to_sort[smallest_number_index]:
                    smallest_number_index = value
                if list_to_sort[-1 - value] > largest_number:
                    largest_number = list_to_sort[-1 - value]

                iterations += 1

            if index != smallest_number_index:
                list_to_sort.insert(index, list_to_sort.pop(smallest_number_index))
            if list_to_sort.index(largest_number) != -1 - index:
                list_to_sort.insert(len(list_to_sort) - (index + 1), list_to_sort.pop(list_to_sort.index(largest_number)))

            index += 1

            update_display(list_to_sort, 15, "Sort 4")

    return iterations

def sort_m(lst):
    start_index_list = [1,0,4,3,0,7,6,10,9,6,0,13,12,16,15,12,19,18,21,23,21,18,12,0,26,25,29,28,25,32,31,35,34,31,25,38,37,41,40,37,44,43,46,48,46,43,37,25,0,51,50,54,53,50,57,56,60,59,56,50,63,62,66,65,62,69,68,71,73,71,68,62,50,76,75,79,78,75,82,81,85,84,81,75,88,87,91,90,87,94,93,96,98,96,93,87,75,50,0]
    iterations = [0]  # Counter for iterations

    def merge(left, right, start_iterator, start_index, return_list):
        result = []
        while (left and right):
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
            iterations[0] += 1
        if left:
            result += left
            iterations[0] += len(left)
        if right:
            result += right
            iterations[0] += len(right)
        start_iterator += 1
        start_index = start_index_list[start_iterator]
        for element in result:
            return_list.remove(element)
            return_list.insert(start_index + result.index(element), element)
            update_display(return_list, 30, "Merge Sort")
        # return_list[start_index:start_index + len(result)] = result
        return result, start_iterator, start_index

    def sort_m2(lst, start_iterator, return_list):
        if len(lst) <= 1:
            return lst, start_iterator, start_index_list[start_iterator - 1]
        middle = len(lst) // 2
        left = lst[:middle]
        right = lst[middle:]
        sleft, start_iterator, start_index = sort_m2(left, start_iterator, return_list)
        sright, start_iterator, _ = sort_m2(right, start_iterator, return_list)
        merged, start_iterator, start_index = merge(sleft, sright, start_iterator, start_index, return_list)
        return merged, start_iterator, start_index

    return_list = lst[:]  # Initialize return list as a copy of the original list
    _, total_iterations, _ = sort_m2(lst, -1, return_list)
    return total_iterations

def sort_bogo(list_to_sort):
    iterations = 0
    while not is_sorted(list_to_sort):
        random.shuffle(list_to_sort)
        iterations += 1
        if keyboard.is_pressed('tab'):
            return -1
        update_display(list_to_sort, 1000000, "Bogo Sort")
    return iterations

main()