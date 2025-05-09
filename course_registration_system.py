# List of all the courses to choose from
ListOf_courses = ["English", "Math", "Python", "Web Design", "Ui/Ux Design", "Data Engineering", "Dba", "Agriculture"]
ListOf_courses.sort()

# All student
all_students = dict()


while True:
    """ask for what student wants to do next
    (R >> Register, RR >> Remove, V >> View and E >> Exit)
    """
    main_programme = input(
        """\n>>> What would you like to do?:\n
    > (R) To Register course\n
    > (E) To Edit registered courses\n
    > (V) To View registered courses\n
    > (Ex) To Exit programme\n"""
    ).title()

    if main_programme == "R":
        while True:
            student_name = str(input(">>> What is your name? (Full name)\n")).title()

            if student_name not in all_students:
                all_students[student_name] = set()
                print(f"\n>>> Congratulations {student_name}, you've been added to the student record. >>>")
            else:
                print(f"\n>>> Welcome back, {student_name}! Your current registered courses are: ")
                for course in all_students[student_name]:
                    print(f"* {course}")

            print("\n>>> List of All Courses Offered")
            for course in ListOf_courses:
                print(f"* {course}")
            print("Register a minimum of 3 courses \n")

            registration_complete = False
            while not registration_complete:
                while True:
                    courseTo_reg = input(
                        '\n>>> Which course would you like to register? (Type "done" to finish)\n'
                    ).title()
                    if courseTo_reg.lower() == "done":
                        if len(all_students[student_name]) >= 3:
                            print(
                                f"\n>>> Registration complete, you registered a total of {len(all_students[student_name])} course(s):"
                            )
                            for course in all_students[student_name]:
                                print(f"* {course}")
                            registration_complete = True
                            break
                        else:
                            print(
                                f">>> You have registered {len(all_students[student_name])} course(s). Register at least 3 to complete.⚠️ "
                            )
                    elif courseTo_reg == "":
                        print(">>> Course name can't be empty. ⚠️")
                    elif courseTo_reg not in ListOf_courses:
                        print(f">>>⚠️ {courseTo_reg} is not in the list of available courses.⚠️")
                    elif courseTo_reg in all_students[student_name]:
                        print(f">>> {courseTo_reg} is already registered. Choose another course.⚠️\n ")
                    else:
                        all_students[student_name].add(courseTo_reg)
                        print(f">>> {courseTo_reg} registered successfully!")
                        break

                    # Only show course list again if input was invalid
                    print("\n>>>✅ Here is the list of available courses again:✅")
                    for course in ListOf_courses:
                        print(f"* {course}")

            optionToRegMore_students = input("\n>>> Register another student? (Y/N)\n").title()
            if optionToRegMore_students != "Y":
                print(">>> Exiting registration... \n")
                break

    # Edit registered courses
    elif main_programme == "E":
        try:
            student_name = str(input(">>> Enter full name view records\n")).title()

            if student_name in all_students:
                print(f">>> {student_name} >>> all registered courses: \n")
                for courses in all_students[student_name]:
                    print(f"* {courses}")

                add_OR_remove = str(input('>>> Type "A" to Add a course OR "R" to remove a course')).title()
                if add_OR_remove == "A":
                    registration_complete = False
                    while not registration_complete:
                        while True:
                            courseTo_add = input(
                                '\n>>> Which course would you like to add? (Type "done" to finish)\n'
                            ).title()

                            if courseTo_add.lower() == "done":
                                if len(all_students[student_name]) >= 3:
                                    print(
                                        f"\n>>> Registration complete, you registered a total of {len(all_students[student_name])} course(s):"
                                    )
                                    for course in all_students[student_name]:
                                        print(f"* {course}")
                                    registration_complete = True
                                    break
                                else:
                                    print(
                                        f">>> You have registered {len(all_students[student_name])} course(s). Register at least 3 to complete. "
                                    )
                            elif courseTo_add == "":
                                print(">>> Course name can't be empty. ")
                            elif courseTo_add not in ListOf_courses:
                                print(f">>> {courseTo_add} is not in the list of available courses.")
                            elif courseTo_add in all_students[student_name]:
                                print(f">>> {courseTo_add} is already registered. Choose another course.\n ")
                            else:
                                all_students[student_name].add(courseTo_add)
                                print(f">>> {courseTo_add} added successfully!")
                                break

                            print("\n>>>✅ Here is the list of available courses again:✅")
                            for course in ListOf_courses:
                                print(f"* {course}")

                    print(">>> Exiting registration... \n")

                elif add_OR_remove == "R":
                    while True:
                        try:
                            courseTo_remove = input(">>> Which course would you like to remove?\n").title()
                        except ValueError:
                            print(">>> Enter course you wish to edit ")

                        if courseTo_remove.lower() == "done":
                            if len(all_students[student_name]) >= 3:
                                print(
                                    f"\n>>> Registration complete, you registered a total of {len(all_students[student_name])} course(s):"
                                )
                                for course in all_students[student_name]:
                                    print(f"* {course}")
                                registration_complete = True
                                break
                            else:
                                print(
                                    f">>> You have registered {len(all_students[student_name])} course(s). Register at least 3 to complete. "
                                )
                        elif courseTo_remove == "":
                            print(">>> Course name can't be empty. ")
                        elif courseTo_remove not in all_students[student_name]:
                            print(f">>> {courseTo_remove} is not in your list of registered courses.")
                        elif courseTo_remove in all_students[student_name]:
                            all_students[student_name].remove(courseTo_remove)
                            print(f">>> {courseTo_remove} removed successfully!")
                            if len(all_students[student_name]) >= 3:
                                break
                            else:
                                registration_complete = False
                                while not registration_complete:
                                    while True:
                                        courseTo_reg = input(
                                            '\n>>> Which course would you like to register? (Type "done" to finish)\n'
                                        ).title()
                                        if courseTo_reg.lower() == "done":
                                            if len(all_students[student_name]) >= 3:
                                                print(
                                                    f"\n>>> Registration complete, you registered a total of {len(all_students[student_name])} course(s):"
                                                )
                                                for course in all_students[student_name]:
                                                    print(f"* {course}")
                                                registration_complete = True
                                                break
                                            else:
                                                print(
                                                    f">>> You have registered {len(all_students[student_name])} course(s). Register at least 3 to complete.⚠️ "
                                                )
                                        elif courseTo_reg == "":
                                            print(">>> Course name can't be empty. ⚠️")
                                        elif courseTo_reg not in ListOf_courses:
                                            print(f">>>⚠️ {courseTo_reg} is not in the list of available courses.⚠️")
                                        elif courseTo_reg in all_students[student_name]:
                                            print(
                                                f">>> {courseTo_reg} is already registered. Choose another course.⚠️\n "
                                            )
                                        else:
                                            all_students[student_name].add(courseTo_reg)
                                            print(f">>> {courseTo_reg} registered successfully!")
                                            break

                                        print("\n>>>✅ Here is the list of available courses again:✅")
                                        for course in ListOf_courses:
                                            print(f"* {course}")
            elif student_name not in all_students:
                print("\n>>> No registered courses or records found\n")
                enroll_or_quit = str(
                    input(">>> New Student?, don't worry😊 type 'Enroll' to start registration or 'Q' to quit:\n")
                ).title()
                if enroll_or_quit == "Enroll":
                    while True:
                        try:
                            student_name = str(input(">>> What is your name? (Full name)\n")).title()

                            if student_name not in all_students:
                                all_students[student_name] = set()
                                print(
                                    f"\n>>> Congratulations {student_name}, you've been added to the student record. >>>"
                                )
                            else:
                                print(f"\n>>> Welcome back, {student_name}! Your current registered courses are: ")
                                for course in all_students[student_name]:
                                    print(f"* {course}")

                            print("\n>>> List of All Courses Offered ")
                            for course in ListOf_courses:
                                print(f"* {course}")
                            print("Register a minimum of 3 courses \n")

                            registration_complete = False
                            while not registration_complete:
                                courseTo_reg = input(
                                    '\n>>> Which course would you like to register? (Type "done" to finish)\n'
                                ).title()

                                if courseTo_reg.lower() == "done":
                                    if len(all_students[student_name]) >= 3:
                                        print(
                                            f"\n>>> Registration complete, you registered a total of {len(all_students[student_name])} course(s):"
                                        )
                                        for course in all_students[student_name]:
                                            print(f"* {course}")
                                        registration_complete = True
                                    else:
                                        print(
                                            f">>> You have registered {len(all_students[student_name])} course(s). Register at least 3 to complete. "
                                        )
                                elif courseTo_reg == "":
                                    print(">>> Course name can't be empty. ")
                                elif courseTo_reg not in ListOf_courses:
                                    print(f">>> {courseTo_reg} is not in the list of available courses.")
                                elif courseTo_reg in all_students[student_name]:
                                    print(f">>> {courseTo_reg} is already registered. Choose another course.\n ")
                                    quickLookUp = input(
                                        ">>> Would you like to see courses you have registered so far?(Y/N):"
                                    ).capitalize()
                                    if quickLookUp != "N":
                                        for course in all_students[student_name]:
                                            print(">>> You have registered:\n")
                                            print(f"* {course}")
                                else:
                                    all_students[student_name].add(courseTo_reg)
                                    print(f">>> {courseTo_reg} registered successfully!")

                            optionToQuit_editting = str(input("Continue editting or quit?(C/Q)")).title()
                            if optionToQuit_editting != "C":
                                print(">>> Exiting registration... \n")
                                break
                        except ValueError:
                            print(">>> Enter your full name to start registeration")
                else:
                    print(">>> REGISTRATION PROCESS ENDING.....")
        except ValueError:
            print(">>> Enter your full name ")

    # View all registered courses
    elif main_programme == "V":
        student_name = str(input(">>> What is your name? (Full name)\n")).title()

        if not all_students:
            print("\n>>> No registered courses or records found")
            enroll_or_quit = str(
                input(">>> New Student?, don't worry😊 type 'Enroll' to start registration:\n")
            ).title()
            if enroll_or_quit == "Enroll":
                while True:
                    student_name = str(input(">>> What is your name? (Full name)\n")).title()

                    if student_name not in all_students:
                        all_students[student_name] = set()
                        print(f"\n>>> Congratulations {student_name}, you've been added to the student record. >>>")
                    else:
                        print(f"\n>>> Welcome back, {student_name}! Your current registered courses are: ")
                        for course in all_students[student_name]:
                            print(f"* {course}")

                    print("\n>>> List of All Courses Offered ")
                    for course in ListOf_courses:
                        print(f"* {course}")
                    print("Register a minimum of 3 courses \n")

                    registration_complete = False
                    while not registration_complete:
                        courseTo_reg = input(
                            '\n>>> Which course would you like to register? (Type "done" to finish)\n'
                        ).title()

                        if courseTo_reg.lower() == "done":
                            if len(all_students[student_name]) >= 3:
                                print(
                                    f"\n>>> Registration complete, you registered a total of {len(all_students[student_name])} course(s):"
                                )
                                for course in all_students[student_name]:
                                    print(f"* {course}")
                                registration_complete = True
                            else:
                                print(
                                    f">>> You have registered {len(all_students[student_name])} course(s). Register at least 3 to complete. "
                                )
                        elif courseTo_reg == "":
                            print(">>> Course name can't be empty. ")
                        elif courseTo_reg not in ListOf_courses:
                            print(f">>> {courseTo_reg} is not in the list of available courses.")
                        elif courseTo_reg in all_students[student_name]:
                            print(f">>> {courseTo_reg} is already registered. Choose another course.\n ")
                            quickLookUp = input(
                                ">>> Would you like to see courses you have registered so far?(Y/N):"
                            ).capitalize()
                            if quickLookUp != "N":
                                for course in all_students[student_name]:
                                    print(">>> You have registered:\n")
                                    print(f"* {course}")
                        else:
                            all_students[student_name].add(courseTo_reg)
                            print(f">>> {courseTo_reg} registered successfully!")

                    optionToRegMore_students = input("\n>>> Register another student? (Y/N)\n").title()
                    if optionToRegMore_students != "Y":
                        print(">>> Exiting registration... \n")
                        break
        else:
            print(f">>> {student_name}, all registered courses: \n")
            for course in all_students[student_name]:
                print(f"* {course}")

        optionToRegMore_courses = input(">>> Would you like to add more courses? (Y/N)").title()

        if optionToRegMore_courses == "Y":
            registration_complete = False
            while not registration_complete:
                courseTo_reg = input('\n>>> Which course would you like to register? (Type "done" to finish)\n').title()

                if courseTo_reg.lower() == "done":
                    if len(all_students[student_name]) >= 3:
                        print(
                            f"\n>>> Registration complete, you registered a total of {len(all_students[student_name])} course(s):"
                        )
                        for course in all_students[student_name]:
                            print(f"* {course}")
                        registration_complete = True
                    else:
                        print(
                            f">>> You have registered {len(all_students[student_name])} course(s). Register at least 3 to complete. "
                        )
                elif courseTo_reg == "":
                    print(">>> Course name can't be empty. ")
                elif courseTo_reg not in ListOf_courses:
                    print(f">>> {courseTo_reg} is not in the list of available courses.")
                elif courseTo_reg in all_students[student_name]:
                    print(f">>> {courseTo_reg} is already registered. Choose another course.\n ")
                    quickLookUp = input(
                        ">>> Would you like to see courses you have registered so far?(Y/N):"
                    ).capitalize()
                    if quickLookUp != "N":
                        print(">>> You have registered:\n")
                        for course in all_students[student_name]:
                            print(f"* {course}")
                else:
                    all_students[student_name].add(courseTo_reg)
                    print(f">>> {courseTo_reg} registered successfully!")
        else:
            print(f">>> YOU REGISTERED TOTAL OF {len(all_students[student_name])} COURSES")
            for course in all_students[student_name]:
                print(f"* {course}")

    elif main_programme == "Ex":
        print(">>> Exiting Course Registration Process now!!!")
        print('>>> Goodbye!!!')
        break
