def admin_only(dashboard):
    def wrapper(username):
        if username == "admin":
            return dashboard(username)
        else:
            print("Access Denied")
    return wrapper  


@admin_only
def dashboard(username):
    print("Login successfully")


dashboard("admin")
dashboard("user")
