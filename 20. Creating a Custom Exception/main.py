import click

class InvalidAgeError(Exception):
    def __init__(self):
        self.message = "Age must be greater than or equal to 18."
        super().__init__(click.style(self.message, fg="red"))


def check_age(age):
    try:
        if age >= 18:
            print(click.style("Valid age.", fg="green"))
        else:
            raise InvalidAgeError()
    except InvalidAgeError as e: 
        print(e)

check_age(18)
check_age(17)