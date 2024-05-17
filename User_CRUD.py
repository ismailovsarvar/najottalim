from typing import Optional
from uuid import UUID, uuid4
from colorama import Fore, Style


class User:
    def __init__(self,
                 _id: Optional[UUID] = None,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 full_name: Optional[str] = None,
                 phone_number: Optional[str] = None,
                 email: Optional[str] = None) -> None:
        self.user_id = _id or uuid4()
        self.username = username
        self.password = password
        self.full_name = full_name
        self.phone_number = phone_number
        self.email = email

    def __str__(self) -> str:
        return self.username


class UserManager:
    def __init__(self):
        self.users = {}

    def create_user(self, username: str, password: str, full_name: Optional[str] = None,
                    phone_number: Optional[str] = None, email: Optional[str] = None) -> User:
        user = User(username=username, password=password, full_name=full_name, phone_number=phone_number, email=email)
        self.users[user.user_id] = user
        return user

    def read_user(self, user_id: UUID) -> Optional[User]:
        return self.users.get(user_id)

    def update_user(self, user_id: UUID, full_name: Optional[str] = None, phone_number: Optional[str] = None,
                    email: Optional[str] = None) -> Optional[User]:
        user = self.users.get(user_id)
        if user:
            if full_name:
                user.full_name = full_name
            if phone_number:
                user.phone_number = phone_number
            if email:
                user.email = email
        return user

    def delete_user(self, user_id: UUID) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False


manager = UserManager()

# Create a new user

user = manager.create_user(username="Sarvar",
                           password="password123",
                           full_name="Ismailov Sarvar",
                           phone_number="+998917826550",
                           email="sarvar@gmail.com")
print(f"{Fore.MAGENTA}Created User:{Style.RESET_ALL}")
print(f"Username: {Fore.GREEN}{user.username}{Style.RESET_ALL}")
print(f"User ID:{Fore.CYAN} {user.user_id}{Style.RESET_ALL}")
print(f"Full Name: {Fore.GREEN}{user.full_name}{Style.RESET_ALL}")
print(f"Phone Number:{Fore.GREEN} {user.phone_number}{Style.RESET_ALL}")
print(f"Email:{Fore.GREEN} {user.email}{Style.RESET_ALL}")

# Read the user's information

read_user = manager.read_user(user.user_id)
if read_user:
    print(f"{Fore.MAGENTA}\nReading User Information:{Style.RESET_ALL}")
    print(f"Username: {Fore.GREEN}{read_user.username}{Style.RESET_ALL}")
    print(f"User ID: {Fore.CYAN}{read_user.user_id}{Style.RESET_ALL}")
    print(f"Full Name: {Fore.GREEN}{read_user.full_name}{Style.RESET_ALL}")
    print(f"Phone Number: {Fore.GREEN}{read_user.phone_number}{Style.RESET_ALL}")
    print(f"Email:{Fore.GREEN} {read_user.email}{Style.RESET_ALL}")

# Update the user's full name and email

updated_user = manager.update_user(user.user_id, full_name="Sardor Gafurov", email="gafurovsardor@gmail.com")
if updated_user:
    print(f"{Style.RESET_ALL}\nUpdated User Information:{Style.RESET_ALL}")
    print(f"Username: {Fore.GREEN}{updated_user.username}{Style.RESET_ALL}")
    print(f"User ID:{Fore.CYAN} {updated_user.user_id}{Style.RESET_ALL}")
    print(f"Full Name:{Fore.GREEN} {updated_user.full_name}{Style.RESET_ALL}")
    print(f"Phone Number:{Fore.GREEN} {updated_user.phone_number}{Style.RESET_ALL}")
    print(f"Email:{Fore.GREEN} {updated_user.email}{Style.RESET_ALL}")

# Delete the user

delete_success = manager.delete_user(user.user_id)
if delete_success:
    print(f"{Fore.MAGENTA}\nUser deleted successfully.{Style.RESET_ALL}")
else:
    print(f"{Fore.MAGENTA}\nFailed to delete user.{Style.RESET_ALL}")
