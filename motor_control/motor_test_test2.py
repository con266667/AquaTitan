import sys

def echo_to_file(st: str):
    original_stdout = sys.stdout
    with open('/dev/pi-blaster', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        print(st)
        sys.stdout = original_stdout  # Reset the standard output to its original value


from time import sleep


echo_to_file("4=0.09")
sleep(1)

for i in range(90, 180, 1):
	print(i / 10)
	echo_to_file("4=" + str(i/1000))
	sleep(0.1)
