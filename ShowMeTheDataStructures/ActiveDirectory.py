class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    if user == None or group == None:
        return False

    for group_user in group.get_users():
        if group_user == user:
            return True

    for sub_group in group.get_groups():
        return is_user_in_group(user, sub_group)

    return False

print('*** Test Active Directory ***')

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
parent_user = "superuser"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_user(parent_user)

print(is_user_in_group(parent_user, None))
assert is_user_in_group(parent_user, None) == False, "None group should return false"

print(is_user_in_group(None, parent))
assert is_user_in_group(None, parent) == False, "None user should return false"

print(is_user_in_group(sub_child_user, parent))
assert is_user_in_group(sub_child_user, parent), "User not found in subgroup!"

print(is_user_in_group(sub_child_user, sub_child))
assert is_user_in_group(sub_child_user, sub_child), "User not found in same group!"

print(is_user_in_group(parent_user, sub_child))
assert is_user_in_group(parent_user, sub_child) == False, "User is only in super group!"

print('*** Success ***')

