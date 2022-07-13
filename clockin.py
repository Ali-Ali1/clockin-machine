import sys 
import argparse
import threading
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def clock_in(bnum, passcode, time):


	if time == "SUMMER":
		s_time = "0:01"
		summer_clockin(bnum ,passcode ,s_time)

		delay = 60
		s_time2 = "0:02"
		clock_out_time = threading.Timer(delay, summer_clockin, [s_time2, bnum, passcode])
		clock_out_time.start()

	else:

		time_machine = "https://timemachine1-vm.berea.edu/ultratime/ultrapunch/login.aspx"

		user_id = "UserID"
		password = "UserPass"
		code = "UserDC"

		summer = "S6720401"

		driver = webdriver.Chrome("./chromedriver")

		driver.get(time_machine)


		driver.find_element_by_id(user_id).send_keys(bnum)
		driver.find_element_by_id(password).send_keys(passcode)
		driver.find_element_by_id(code).send_keys(summer)

		driver.find_element_by_id("BUTIN").click()

		

		
		
		clock_out_after(time, bnum, passcode)

		


		


def clock_out(bnum, passcode):


	time_machine = "https://timemachine1-vm.berea.edu/ultratime/ultrapunch/login.aspx"

	user_id = "UserID"
	password = "UserPass"

	driver = webdriver.Chrome("./chromedriver")

	driver.get(time_machine)


	driver.find_element_by_id(user_id).send_keys(bnum)
	driver.find_element_by_id(password).send_keys(passcode)

	driver.find_element_by_id("BUTOUT").click()

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")

	print("You are clocked OUT ... ", current_time)

	

def clock_out_after(time, bnum, passcode):
	
	delay = time
	out_time = delay.split(":")
	delay = int((int(out_time[0]) * 3600) + int(out_time[1]) * 60)

	clock_out_time = threading.Timer(delay, clock_out, [bnum, passcode])
	clock_out_time.start()

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")


	print("You are clocked IN ... ", current_time)

def summer_out_after(time, bnum, passcode):
	
	delay = time
	out_time = delay.split(":")
	delay = int((int(out_time[0]) * 3600) + int(out_time[1]) * 60)

	clock_out_time = threading.Timer(delay, summer_out, [bnum, passcode])
	clock_out_time.start()

	now = datetime.now()
	current_time = now.strftime("%H:%M:%S")


	print("You are clocked IN ... ", current_time)

def summer_in(bnum, passcode, time):
	time_machine = "https://timemachine1-vm.berea.edu/ultratime/ultrapunch/login.aspx"

	user_id = "UserID"
	password = "UserPass"
	code = "UserDC"

	summer = "S6720401"

	driver = webdriver.Chrome("./chromedriver")

	driver.get(time_machine)


	driver.find_element_by_id(user_id).send_keys(bnum)
	driver.find_element_by_id(password).send_keys(passcode)
	driver.find_element_by_id(code).send_keys(summer)

	driver.find_element_by_id("BUTIN").click()

	
	summer_out_after(time, bnum, passcode)


if __name__ == "__main__": 
	msg="A program to clock in and out hustle-free"
	parser = argparse.ArgumentParser(description= msg)
	parser.add_argument("-bnum", "--BNUM", help="bnumber without the 'b'")
	parser.add_argument("-p", "--PASS", help="the login password")
	parser.add_argument("-after", "--AFTER", help="input time to be clocked out after[-t HOURs:MINs], ex. -t 1:30 'meaning after one hour and 30 mins'")

	args= vars(parser.parse_args(sys.argv[1:]))

	#warning to provide the date and filename
	if not args["PASS"]:
		print("please provide the password ex. -p 1234")
	if not args["BNUM"]:
		print("please provide the bnum ex. -bnum 00123456")
	if not args["AFTER"]:
		print("input time to be clocked out after[-t HOURs:MINs], ex. -t 1:30 'meaning after one hour and 30 mins'")


	#if everything looks good :)
	else:
		clock_in(args["BNUM"], args["PASS"], args["AFTER"])
		


