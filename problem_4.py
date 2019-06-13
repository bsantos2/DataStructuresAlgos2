class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []
        self.directory = {}

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_name(self):
        return self.name()

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

def is_user_in_group(user, group):
    node = group.directory
    node[group.name] = group.users
    if user in group.users:
        return True
    elif not group.groups:
        return False
    else:
        for each_group in group.groups:
            node = each_group
            return is_user_in_group(user, node)

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)
#Case 1
#output - > True, because the user resides in sub_child group
activeDirectory = is_user_in_group("sub_child_user", sub_child)
print("Case 1")
print(activeDirectory)

#Case 2
#output - > True, parent is above child, then subchild groups. It was able to find through
#the subgroups eventually, the name of the user
activeDirectory = is_user_in_group("sub_child_user", parent)
print("Case 2")
print(activeDirectory)

#Case 3
#output - > False, batman is nowhere to be found on any of the groups and subgroups
activeDirectory = is_user_in_group("batman", parent)
print("Case 3 ")
print(activeDirectory)

