import cmd
import secrets
import string
import random
from strength import check_strength


def generate_password(min_length, numbers=True, special_char=True, use_upper=True, use_lower=True):
    
    letters = ""
    if use_lower:
        letters += string.ascii_lowercase
    if use_upper:
        letters += string.ascii_uppercase

    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_char:
        characters += special

    pwd = []
    has_number = False
    has_special = False
    has_letter = False

    while (
        len(pwd) < min_length or
        (numbers and not has_number) or
        (special_char and not has_special) or
        ((use_upper or use_lower) and not has_letter)
        ):

        new_char = secrets.choice(characters)
        pwd.append(new_char)

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        elif new_char in letters:
            has_letter = True

    random.shuffle(pwd)
    return "".join(pwd)


class PasswordConsole(cmd.Cmd):
    intro = """
        ========================================
            Secure Password Generator CLI
        ========================================
        Type 'help' to view commands.
        """
    prompt = "PassGen> "

    def do_generate(self, arg):
        
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("[-] Length must be greater than 0.")
                return

            numbers = input("Include numbers? (y/n): ").lower() == 'y'
            special = input("Include special characters? (y/n): ").lower() == 'y'
            upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
            lower = input("Include lowercase letters? (y/n): ").lower() == 'y'

            if not any([numbers, special, upper, lower]):
                print("[-] Select at least one character type.")
                return

            self.last_password = generate_password(length, numbers, special, upper, lower)

            print(f"\n[+] Generated Password: {self.last_password}")
            
        except ValueError:
            print("[-] Invalid input. Length must be a number.")

    def do_check(self, arg):

        if arg:
            password = arg.strip()
        elif hasattr(self, 'last_password'):
            choice = input("Check last generated password? (y/n): ").lower()
            if choice == 'y':
                password = self.last_password
            else:
                password = input("Enter password to check: ")
        else:
            password = input("Enter password to check: ")

        strength = check_strength(password)

        print(f"\n[+] Password: {password}")
        print(f"[+] Strength: {strength}")

    def do_save(self, arg):

        if not hasattr(self, 'last_password'):
            print("[-] No password to save")
            return

        print(f"[+] Current Password: {self.last_password}")

        filename = input("Enter filename (default: password.txt): ").strip()
        if not filename:
            filename = "password.txt"

        mode = input("Append or overwrite? (a/o): ").lower()

        if mode not in ['a', 'o']:
            print("[-] Invalid option. Using append mode.")
            file_mode = "a"
        elif mode == 'o':
            file_mode = "w"
        else:
            file_mode = "a"
            
        try:
            with open(filename, file_mode) as f:
                 f.write(self.last_password + "\n")

            print(f"[+] Password saved to {filename}")
            
        except Exception as e:
             print(f"[-] Error saving file: {e}")

    def do_exit(self, arg):
        print("Exiting...")
        return True
    
    def do_help(self, arg):

        print("""
	========================================
		Secure Password Generator
	========================================

	Commands:

	generate   -> Generate a new secure password
	check      -> Check password strength
	save       -> Save generated password
	help       -> Show help menu
	exit       -> Exit application

	========================================
	""")


if __name__ == "__main__":
    PasswordConsole().cmdloop()
