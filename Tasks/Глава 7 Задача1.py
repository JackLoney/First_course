def santa_users(users_list):
    users_dict = {}
    for user in users_list:
        if len(user) == 1:
            name = user[0]
            index = None
        else:
            name, index = user
        users_dict[name] = index
    return users_dict

def main():
    users = [["name1 surname1", 12345], ["name2 surname2"], ["name3 surname3", 12354], ["name4 surname4", 12435]]
    result = santa_users(users)
    print(result)
if __name__ == "__main__":
    main()
