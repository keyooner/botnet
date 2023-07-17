import temp
import FirebaseFunctions.firebaseDatabase as fdb
import FirebaseFunctions.firebaseAuthentication as fba
import re

email_global_user = temp.get_email()
password_global_user = temp.get_password()

values_unlocked = fdb.get_values_unlocked(email_global_user, password_global_user)
values_locked = fdb.get_values_locked(email_global_user, password_global_user)
count_values_unlocked = fdb.get_count_values_unlocked(email_global_user, password_global_user)
count_values_locked = fdb.get_count_values_locked(email_global_user, password_global_user)
count_values_follow = None
count_values_for_actions = None
values_comment = None
values_like = None
values_rt = None
values_follow = None

def get_logout():
    fba.logOutUser()

def set_load_values_actions(url, data, user):
    link = split_url_actions(url)
    fdb.loadValuesActionsTwitter(email_global_user, password_global_user, link, data, user)

def set_load_values_follow(url, data, user):
    username = split_url_follow(url)
    fdb.loadValuesFollow(email_global_user, password_global_user, username, data, user)

def set_values_follow(url, button_entry_get):
    global values_follow
    values_follow = fdb.get_values_for_follow(email_global_user, password_global_user, split_url_follow(url), button_entry_get)

def get_values_follow():
    return values_follow

def update_values_follow(url, button_entry_get):
    set_values_follow(url, button_entry_get)
    return values_follow

def set_values_like(url, button_entry_get):
    global values_like
    values_like = fdb.get_values_for_like(email_global_user, password_global_user, split_url_actions(url), button_entry_get)

def get_values_like():
    return values_like

def update_values_like(url, button_entry_get):
    set_values_like(url, button_entry_get)
    return values_like

def set_values_rt(url, button_entry_get):
    global values_rt
    values_rt = fdb.get_values_for_rt(email_global_user, password_global_user, split_url_actions(url), button_entry_get)

def get_values_rt():
    return values_rt

def update_values_rt(url, button_entry_get):
    set_values_rt(url, button_entry_get)
    return values_rt

def set_values_comment(url, button_entry_get):
    global values_comment
    values_comment = fdb.get_values_for_comment(email_global_user, password_global_user, split_url_actions(url), button_entry_get)

def get_values_comment():
    return values_comment

def update_values_comment(url, button_entry_get):
    set_values_comment(url, button_entry_get)
    return values_comment

def set_count_values_actions(url):
    global count_values_for_actions
    count_values_for_actions = fdb.get_count_values_for_actions(email_global_user, password_global_user, split_url_actions(url))

def get_count_values_actions():
    return count_values_for_actions

def update_count_values_actions(url):
    set_count_values_actions(url)
    return count_values_for_actions

def set_count_values_follow(url):
    global count_values_follow
    count_values_follow = fdb.get_count_values_for_follow(email_global_user, password_global_user, split_url_follow(url))

def get_count_values_follow():
    return count_values_follow

def update_count_values_follow(url):
    set_count_values_follow(url)
    return count_values_follow

def update_values_unlocked_ff():
    set_values_unlocked_ff()
    return values_unlocked

def update_values_locked_ff():
    set_values_locked_ff()
    return values_locked

def set_values_unlocked_ff():
    global values_unlocked
    values_unlocked = fdb.get_values_unlocked(email_global_user, password_global_user)
    
def get_values_unlocked_ff():
    return values_unlocked

def set_values_locked_ff():
    global values_locked
    values_locked = fdb.get_values_locked(email_global_user, password_global_user)
    
def get_values_locked_ff():
    return values_locked

def set_count_values_unlocked_ff():
    global count_values_unlocked
    count_values_unlocked = fdb.get_count_values_unlocked(email_global_user, password_global_user)
    
def get_count_values_unlocked_ff():
    return count_values_unlocked

def set_count_values_locked_ff():
    global count_values_locked
    count_values_locked = fdb.get_count_values_locked(email_global_user, password_global_user)
    
def get_count_values_locked_ff():
    return count_values_locked

def split_url_actions(url):
        pattern = r"(https://twitter.com/)([A-Za-z0-9_]+)(/status/)([0-9]+)"
        if not (matches := re.search(pattern, url)):
                return None
        username = matches[2]
        return f"{username}-{matches[4]}"

def split_url_follow(url):
        pattern = r"(https://twitter.com/)([A-Za-z0-9_]+)"
        return matches[2] if (matches := re.search(pattern, url)) else None
    
def set_preferences(data):
    fdb.loadValuesPreferences(email_global_user, password_global_user, data)

def get_preferences():
    return fdb.getValuesPreferences(email_global_user, password_global_user)

def get_last_user_create():
    return fdb.getLastValueUser(email_global_user, password_global_user)

def get_last_email_create():
    return fdb.getLastValueEmail(email_global_user, password_global_user)

def deleteValues():
    fdb.deleteValues(email_global_user, password_global_user)