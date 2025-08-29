username1 = "Zfike0182"
username2 = "User2Name"

password1 = "ZachPassw0rd"
password2 = "User2p@assword"

role_admin = "admin"
role_user = "user"

def calendar(role):
    if role == "admin":
        print("You have an administrator meeting on September 9th")
    elif role == "user":
        print("There is a major service update on September 3rd")
        print("An announcement planned for Spetember 13th")
#This code is simply showing the difference in events for an Admin and a normal User as the admin has a meeting to attend soon, but the User does not and thusly doesn't know about the meeting.

def user_permissions(role):
    if role == "admin":
        print("Your permissions as admin are: \nRequest for administrator meeting \nEditing permissions for user role \nLocking user accounts \nResponding to support tickets \nYou are granted permissions of User role as well")
    elif role == "user":
        print("You permissions as user are: \nCreating support tickets for your problems \nRequesting and viewing files \nViewing your calendar \nMessaging other users")
#This function tells the user what permissions they have with their current role, showing an example of limited access based off their role.

def get_role(username, password):
    if username == "Zfike0182" and password == "ZachPassw0rd":
        role = "admin"
    elif username == "User2Name" and password == "User2p@assword":
        role = "user"
    return role
#Here the code matches the login info with the appropriate role

#With the Calendar and User permissions functions, it shows us Confidentiality as info is only shared to those who need or may use it.
#Admins can have access to whatever they may need, but Users do not need to know or do certain things as that could pose security risks or redundancies.
login_name = str(input("Enter your username: "))
login_password = str(input("Enter your password: "))

current_role = get_role(login_name, login_password)
user_permissions(current_role)
calendar(current_role)