import time

num = 1
while True:
    num += 1
    with open('test.txt', 'w') as file:
        # Write the content to the file
        file.write(str(num))
        print(num)
        time.sleep(1)
