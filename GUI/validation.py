# todo: write function to compare if enter password and confirm password are the same
# todo: write method to check if username/email/phone number is already registered
# TODO: https://stackoverflow.com/questions/37006772/how-to-disable-a-button-unless-a-edit-field-isnt-empty

import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
from validate_email import validate_email
from password_strength import PasswordPolicy
import messageBox

global e


# a function to validate passwords
def passwordValidator(input, confirm):
	policy = PasswordPolicy.from_names(
		length=6,
		uppercase=1,
		numbers=1,
		special=0,
		nonletters=1,
	)

	if not policy.test(input):
		e = 3
		return messageBox.window(e)
	else:
		if input == confirm:
			return True
		else:
			return False


# function validates emails
def email_validator(mail):
	# email_regex = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")

	# if check_blank_fields(mail) == False:
	# if not re.match(mail):
	# return False

	if validate_email(mail):
		return True
	else:
		e = 2
		return messageBox.window(e)


# function validates phone number
def phone_number_validator(num):
	# phone_regex = re.compile(r'^(?:\+?44)?[07]\d{9,13}$')

	# if check_blank_fields(num) == False:
	# if not re.match(num):
	# return False

	if carrier._is_mobile(number_type(phonenumbers.parse(num))):
		return True
	else:
		e = 4
		return messageBox.window(e)


def check_username(username):
	# TODO: create username policy
	if len(str(username)) > 0:
		return True
	else:
		return False


def validate_input(username, email, phonenumber, pwd_in, pwd_conf):
	if check_username(username) and email_validator(email) or phone_number_validator(phonenumber):
		if passwordValidator(pwd_in, pwd_conf):
			return True
	else:
		return False
