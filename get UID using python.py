import pwd

def get_uid(username):
    try:
        user_info = pwd.getpwnam(username)
        return user_info.pw_uid
    except KeyError:
        return None  # Если пользователь не найден

# Указываем имя пользователя, UID которого нужно получить
username = 'имя_пользователя'
uid = get_uid(username)

if uid is not None:
    print(f"UID пользователя {username}: {uid}")
else:
    print(f"Пользователь {username} не найден")
