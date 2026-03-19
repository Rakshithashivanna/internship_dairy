def admin_only(dashboard):
    def wrapper(username):
        if username == "admin":
            print("Login successfully")
            dashboard(username)
        else:
            print("Access Denied")
    return wrapper  


@admin_only
def dashboard(username):
    print("Welcome to the dashboard")


dashboard("admin")
dashboard("user")
