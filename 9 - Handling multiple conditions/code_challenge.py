# Ask a user their name
first_name = input('Enter your first name: ')
first_name_initial = first_name[0:1].upper()

# If their first name starts with A or B 
# tell them they go to room AB
if first_name_initial in ('A', 'B'):
    print('Go to room AB')
# IF their first name starts with C
# tell them to go to room CD
elif first_name_initial in ('C', 'D'):
    print('Go to room CD')
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
else:
    last_name = input('Enter your last name: ')
    last_name_initial = last_name[0:1].upper()
    if last_name_initial == 'Z':
        print('Go to room Z')
    else:
        print('Go to room OTHER')


# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z