# make a list to hold onto our items
shopping_list = []

def show_help():
    # print out instructions on how to use the app
    print("What should we pick up at the store?")
    print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list
""")

# print out the list
def show_list():
    print("Here's your list:")
    for item in shopping_list:
        print(item)
# add item to list
def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item,len(shopping_list)))
show_help()

while True:
    # ask for new items
    new_item = input("> ")

    # be able to quit the app
    if new_item == "DONE":
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    # add new items to our list
    add_to_list(new_item)
