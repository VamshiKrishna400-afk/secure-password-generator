# Secure-password-generator
Secure CLI-based password generator and strength checker built with Python.

# Secure Password Generator CLI

A Python-based command-line password generator designed with cybersecurity best practices.  
This tool generates strong random passwords and checks password strength.

---

## Features

- Generate secure passwords
- Include/exclude:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Password strength checker
- Save generated passwords to file
- Interactive command-line interface

---

## Technologies Used

- Python 3
- secrets module
- random module
- string module
- cmd module

---

## Installation

```bash
git clone https://github.com/yourusername/secure-password-generator.git
cd secure-password-generator
python3 main.py
```

---

## Usage

Display all commands:
```bash
help
```

Generate password:
```bash
generate
```

Check password strength:
```bash
check
```

Save password:
```bash
save
```

Exit:
```bash
exit
```

---

## Example Output

```text
PassGen> generate

Enter password length: 12
Include numbers? (y/n): y
Include special characters? (y/n): y
Include uppercase letters? (y/n): y
Include lowercase letters? (y/n): y

[+] Generated Password: A#9xP!2LmQ@
```

---

## Randomness and Security

This project uses both Python's `secrets` and `random` modules.

### `secrets` Module
Used for:
- Secure password character generation

Why:
- Designed for cryptographic and security-related applications
- Generates unpredictable random values
- Recommended for passwords and authentication systems

### `random` Module
Used for:
- Shuffling password characters before final output

Why:
- Helps randomize character positions
- Suitable for non-cryptographic operations like ordering/shuffling

### Security Note
Sensitive password generation is handled using `secrets.choice()` to ensure stronger security compared to using only the `random` module.
### Security Advantage
Using `random` for password generation can make passwords easier to predict, while `secrets` provides stronger protection against attacks.

## Future Improvements

- GUI version
- Password encryption
- Password vault support
- Export to encrypted files
- Hashing support

---

## Author

Vamshi Krishna GK
<br>
Cybersecurity Enthusiast
