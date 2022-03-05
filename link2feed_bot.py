from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from selenium.webdriver.common.keys import Keys
import pandas as pd

def main():
    web = webdriver.Chrome(ChromeDriverManager().install())
    web.get('')

    time.sleep(1)

    canadian_login = web.find_element_by_xpath('//*[@id="page-content"]/div[3]/div[1]/div/div/div/div/h5/a')
    canadian_login.click()

    #Input your Login Information
    Email = ""
    email = web.find_element_by_xpath('//*[@id="user_email"]')
    email.send_keys(Email)

    #Input your Login Information
    Password = ""
    password = web.find_element_by_xpath('//*[@id="user_password"]')
    password.send_keys(Password)

    log_in = web.find_element_by_xpath('//*[@id="new_user"]/div[3]/input')
    log_in.click()

    # 3. Client Intake Click
    client_intake = web.find_element_by_xpath('//*[@id="linked_app_1"]/div/div/p[1]')
    client_intake.click()

    # 4. New Client
    new_client = web.find_element_by_xpath('//*[@id="new-client"]')
    new_client.click()

    # 5. Program reads data from an excel spreadsheet
    csv_reader = pd.read_csv('')

    # 6. Main program, loops through all values of the excel spreadsheet
    for ind, row in csv_reader.iterrows():
        # each index and row in the csv file

        def final():
            time.sleep(1)
            save2 = web.find_element_by_xpath('//*[@id="intake-wizard-next-btn"]')
            save2.click()

            highest_education = web.find_element_by_xpath(
                '//*[@id="intake_profile_type"]/div[1]/div/div/div/div/div[4]/div')
            highest_education.click()

            save6 = web.find_element_by_xpath('//*[@id="intake-wizard-next-btn"]')
            save6.click()

            time.sleep(2)

            add_element = web.find_element_by_xpath(
                '/html/body/div[1]/div[3]/div[2]/div[2]/form/div[1]/div/div/div[3]/div[2]/div[4]/div/button')
            add_element.click()

            Income = "Other (Specify)"
            income_type = web.find_element_by_xpath(
                '/html/body/div[1]/div[3]/div[2]/div[2]/form/div[1]/div/div/div[3]/div[2]/div[3]/div/div/div/div[2]/div/a')
            income_type.click()
            income_type2 = web.find_element_by_xpath('/html/body/div[8]/div/input')
            income_type2.send_keys(Income)
            income_type2.send_keys(Keys.ENTER)
            Income2 = "0"
            income_type3 = web.find_element_by_xpath(
                '/html/body/div[1]/div[3]/div[2]/div[2]/form/div[1]/div/div/div[3]/div[2]/div[3]/div/div/div/div[2]/input')
            income_type3.send_keys(Income2)
            dot = web.find_element_by_xpath(
                '/html/body/div[1]/div[3]/div[2]/div[2]/form/div[1]/div/div/div[3]/div[2]/div[3]/div/div/div/div[1]')
            dot.click()

            save3 = web.find_element_by_xpath('//*[@id="intake-wizard-next-btn"]')
            save3.click()

            save4 = web.find_element_by_xpath('//*[@id="intake-wizard-next-btn"]')
            save4.click()

            christmas_program_button = web.find_element_by_xpath(
                '//*[@id="available-program-list"]/div[1]/div[3]/div/div')
            christmas_program_button.click()

            # Information for appointments can be set here

            referrals = web.find_element_by_xpath(
                '//*[@id="form-referrals"]/div[2]/div/div/div/div[31]/label')
            referrals.click()
            Referrals = "N/A"
            referrals2 = web.find_element_by_xpath('//*[@id="form-referrer-1666-other"]')
            referrals2.send_keys(Referrals)

            time.sleep(1)

            save5 = web.find_element_by_xpath('//*[@id="form-program-visit"]/div[8]/div/div/button')
            save5.click()

            # Restarting the program
            print("")
            print("")
            print("")
            restart = input("Do you wish to start again: ").lower()
            if restart == "yes":
                main()
            else:
                exit()

        def main_2():
            time.sleep(5)
            household1 = web.find_element_by_xpath('//*[@id="hhm"]/div/div/div[1]/div/a')
            household1.click()
            time.sleep(2)

            child1_first = web.find_element_by_xpath('//*[@id="intake_household_member_type_firstName"]')
            child1_first.send_keys(row['Child 1 First Name'])

            child1_last = web.find_element_by_xpath('//*[@id="intake_household_member_type_lastName"]')
            child1_last.send_keys(row['Child 1 Last Name'])

            time.sleep(1)

            child1_birthdate = web.find_element_by_xpath('//*[@id="intake_household_member_type_dateOfBirth"]')
            child1_birthdate.click()
            child1_birthdate.send_keys(row['Child 1 Birthdate'])
            child1_birthdate.send_keys(Keys.ENTER)

            child1_gender = web.find_element_by_xpath('//*[@id="s2id_intake_household_member_type_gender"]/a')
            child1_gender.click()
            child1_gender.send_keys(row['Child 1 Gender'])
            child1_gender2 = web.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
            child1_gender2.send_keys(Keys.ENTER)

            time.sleep(1)

            child1_disability = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[5]/div/div/div/div/div[2]/div[1]')
            child1_disability.click()

            child1_canadian_citizen = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[6]/div/div/div/div/div[2]/div[1]')
            child1_canadian_citizen.click()

            child1_ethnicity = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[1]/div/div/div/div[4]/div[2]')
            child1_ethnicity.click()

            child1_self_identify = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[2]/div/div/div/div[3]/div[2]')
            child1_self_identify.click()

            time.sleep(1)

            child1_relationship = web.find_element_by_xpath(
                '/html/body/div[1]/div[3]/div[2]/div[2]/div[7]/div/div/form/div[2]/div[2]/div[4]/div/div/a')
            child1_relationship.click()
            relationship = "Child"

            time.sleep(1)

            child1_relationship2 = web.find_element_by_xpath('/html/body/div[13]/div/input')
            child1_relationship2.send_keys(relationship)
            child1_relationship2.send_keys(Keys.ENTER)

            time.sleep(1)

            save3 = web.find_element_by_xpath('//*[@id="hh-member-save-button"]')
            save3.click()

            time.sleep(3)

            print("")
            print("")
            print("")
            continue3 = input("Do you wish to add another child (This is Child 1): ").lower()
            if continue3 == "yes":
                main_3()
            elif continue3 == "no":
                final()
            elif continue3 == "exit":
                exit()

        def main_3():
            time.sleep(1)
            household2 = web.find_element_by_xpath('//*[@id="hhm"]/div/div/div[1]/div/a')
            household2.click()
            time.sleep(2)

            child2_first = web.find_element_by_xpath('//*[@id="intake_household_member_type_firstName"]')
            child2_first.send_keys(row['Child 2 First Name'])

            child2_last = web.find_element_by_xpath('//*[@id="intake_household_member_type_lastName"]')
            child2_last.send_keys(row['Child 2 Last Name'])

            time.sleep(1)

            child2_birthdate = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type_dateOfBirth"]')
            child2_birthdate.click()
            child2_birthdate.send_keys(row['Child 2 Birthdate'])
            child2_birthdate.send_keys(Keys.ENTER)

            child2_gender = web.find_element_by_xpath(
                '//*[@id="s2id_intake_household_member_type_gender"]/a')
            child2_gender.click()
            child2_gender.send_keys(row['Child 2 Gender'])
            child2_gender2 = web.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
            child2_gender2.send_keys(Keys.ENTER)

            time.sleep(1)

            child2_disability = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[5]/div/div/div/div/div[2]/div[1]')
            child2_disability.click()

            child2_canadian_citizen = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[6]/div/div/div/div/div[2]/div[1]')
            child2_canadian_citizen.click()

            child2_ethnicity = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[1]/div/div/div/div[4]/div[2]')
            child2_ethnicity.click()

            child2_self_identify = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[2]/div/div/div/div[3]/div[2]')
            child2_self_identify.click()

            time.sleep(1)

            print("")
            print("")
            print("")
            continue2 = input("Please click the relationship status (child) and write yes: ").lower()

            if continue2 =="yes":
                time.sleep(1)
                save3 = web.find_element_by_xpath('//*[@id="hh-member-save-button"]')
                save3.click()

                time.sleep(2)

                print("")
                print("")
                print("")
                continue4 = input("Do you wish to add another child (This is Child 2): ").lower()
                if continue4 == "yes":
                    main_4()
                elif continue4 == "no":
                    final()
                elif continue4 == "exit":
                    exit()

        def main_4():
            time.sleep(1)

            household3 = web.find_element_by_xpath('//*[@id="hhm"]/div/div/div[1]/div/a')
            household3.click()
            time.sleep(2)

            child3_first = web.find_element_by_xpath('//*[@id="intake_household_member_type_firstName"]')
            child3_first.send_keys(row['Child 3 First Name'])

            child3_last = web.find_element_by_xpath('//*[@id="intake_household_member_type_lastName"]')
            child3_last.send_keys(row['Child 3 Last Name'])

            time.sleep(1)

            child3_birthdate = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type_dateOfBirth"]')
            child3_birthdate.click()
            child3_birthdate.send_keys(row['Child 3 Birthdate'])
            child3_birthdate.send_keys(Keys.ENTER)

            child3_gender = web.find_element_by_xpath(
                '//*[@id="s2id_intake_household_member_type_gender"]/a')
            child3_gender.click()
            child3_gender.send_keys(row['Child 3 Gender'])
            child3_gender2 = web.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
            child3_gender2.send_keys(Keys.ENTER)

            time.sleep(1)

            child3_disability = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[5]/div/div/div/div/div[2]/div[1]')
            child3_disability.click()

            child3_canadian_citizen = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[6]/div/div/div/div/div[2]/div[1]')
            child3_canadian_citizen.click()

            child3_ethnicity = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[1]/div/div/div/div[4]/div[2]')
            child3_ethnicity.click()

            child3_self_identify = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[2]/div/div/div/div[3]/div[2]')
            child3_self_identify.click()

            time.sleep(1)

            print("")
            print("")
            print("")
            continue2 = input("Please click the relationship status (child) and write yes: ").lower()

            if continue2 == "yes":
                time.sleep(1)
                save3 = web.find_element_by_xpath('//*[@id="hh-member-save-button"]')
                save3.click()

                time.sleep(2)

                save3 = web.find_element_by_xpath('//*[@id="hh-member-save-button"]')
                save3.click()

                time.sleep(2)

                print("")
                print("")
                print("")
                continue5 = input("Do you wish to add another child (This is Child 3): ").lower()
                if continue5 == "yes":
                    main_4()
                elif continue5 == "no":
                    final()
                elif continue5 == "exit":
                    exit()

        def main_5():
            time.sleep(1)

            household4 = web.find_element_by_xpath('//*[@id="hhm"]/div/div/div[1]/div/a')
            household4.click()
            time.sleep(2)

            child4_first = web.find_element_by_xpath('//*[@id="intake_household_member_type_firstName"]')
            child4_first.send_keys(row['Child 4 First Name'])

            child4_last = web.find_element_by_xpath('//*[@id="intake_household_member_type_lastName"]')
            child4_last.send_keys(row['Child 4 Last Name'])

            time.sleep(1)

            child4_birthdate = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type_dateOfBirth"]')
            child4_birthdate.click()
            child4_birthdate.send_keys(row['Child 4 Birthdate'])
            child4_birthdate.send_keys(Keys.ENTER)

            child4_gender = web.find_element_by_xpath(
                '//*[@id="s2id_intake_household_member_type_gender"]/a')
            child4_gender.click()
            child4_gender.send_keys(row['Child 4 Gender'])
            child4_gender2 = web.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
            child4_gender2.send_keys(Keys.ENTER)

            time.sleep(1)

            child4_disability = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[5]/div/div/div/div/div[2]/div[1]')
            child4_disability.click()

            child4_canadian_citizen = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[6]/div/div/div/div/div[2]/div[1]')
            child4_canadian_citizen.click()

            child4_ethnicity = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[1]/div/div/div/div[4]/div[2]')
            child4_ethnicity.click()

            child4_self_identify = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[2]/div/div/div/div[3]/div[2]')
            child4_self_identify.click()

            time.sleep(1)

            print("")
            print("")
            print("")
            continue2 = input("Please click the relationship status (child) and write yes: ").lower()

            if continue2 == "yes":
                time.sleep(1)
                save3 = web.find_element_by_xpath('//*[@id="hh-member-save-button"]')
                save3.click()

                time.sleep(2)

                save3 = web.find_element_by_xpath('//*[@id="hh-member-save-button"]')
                save3.click()

                time.sleep(2)

                print("")
                print("")
                print("")
                continue6 = input("Do you wish to add another child (This is Child 4): ").lower()
                if continue6 == "yes":
                    main_5()
                elif continue6 == "no":
                    final()
                elif continue6 == "exit":
                    exit()

        def main_6():
            time.sleep(1)

            household4 = web.find_element_by_xpath('//*[@id="hhm"]/div/div/div[1]/div/a')
            household4.click()
            time.sleep(2)

            child4_first = web.find_element_by_xpath('//*[@id="intake_household_member_type_firstName"]')
            child4_first.send_keys(row['Child 4 First Name'])

            child4_last = web.find_element_by_xpath('//*[@id="intake_household_member_type_lastName"]')
            child4_last.send_keys(row['Child 4 Last Name'])

            time.sleep(1)

            child4_birthdate = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type_dateOfBirth"]')
            child4_birthdate.click()
            child4_birthdate.send_keys(row['Child 4 Birthdate'])
            child4_birthdate.send_keys(Keys.ENTER)

            child4_gender = web.find_element_by_xpath(
                '//*[@id="s2id_intake_household_member_type_gender"]/a')
            child4_gender.click()
            child4_gender.send_keys(row['Child 4 Gender'])
            child4_gender2 = web.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
            child4_gender2.send_keys(Keys.ENTER)

            time.sleep(1)

            child4_disability = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[5]/div/div/div/div/div[2]/div[1]')
            child4_disability.click()

            child4_canadian_citizen = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[6]/div/div/div/div/div[2]/div[1]')
            child4_canadian_citizen.click()

            child4_ethnicity = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[1]/div/div/div/div[4]/div[2]')
            child4_ethnicity.click()

            child4_self_identify = web.find_element_by_xpath(
                '//*[@id="intake_household_member_type"]/div[2]/div[7]/div[2]/div/div/div/div[3]/div[2]')
            child4_self_identify.click()

            time.sleep(1)

            print("")
            print("")
            print("")
            continue2 = input("Please click the relationship status (child) and write yes: ").lower()

            if continue2 == "yes":
                time.sleep(1)
                save3 = web.find_element_by_xpath('//*[@id="hh-member-save-button"]')
                save3.click()

                time.sleep(2)

                save3 = web.find_element_by_xpath('//*[@id="hh-member-save-button"]')
                save3.click()

                time.sleep(2)
                print("")
                print("")
                print("")
                continue7 = input("Do you wish to add another child (This is Child 5): ").lower()
                if continue7 == "yes":
                    main_6()
                elif continue7 == "no":
                    final()
                elif continue7 == "exit":
                    exit()

    time.sleep(2)

    first_food_visit = web.find_element_by_xpath(
        '//*[@id="s2id_intake_personal_type_firstFoodBankVisit_selector"]/a')
    first_food_visit.click()
    Food = "Unknown"
    first_food_visit2 = web.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
    first_food_visit2.send_keys(Food)
    first_food_visit2.send_keys(Keys.ENTER)

    first = web.find_element_by_xpath('//*[@id="intake_personal_type_firstName"]')
    first.send_keys(row['First Name'])

    last = web.find_element_by_xpath('//*[@id="intake_personal_type_lastName"]')
    last.send_keys(row['Last Name'])

    gender = web.find_element_by_xpath('//*[@id="s2id_intake_personal_type_gender"]/a')
    gender.click()
    gender.send_keys(row['Gender'])
    gender2 = web.find_element_by_xpath('//*[@id="select2-drop"]/ul/li/div')
    gender2.click()

    birthdate = web.find_element_by_xpath('//*[@id="intake_personal_type_dateOfBirth"]')
    birthdate.click()
    birthdate.send_keys(row['Birthdate'])
    first.click()

    consent_signature = web.find_element_by_xpath('//*[@id="consent_signature_button"]')
    consent_signature.click()

    time.sleep(1)

    consent_signature2 = web.find_element_by_xpath('//*[@id="visit_form-form-esig-signature-typed_signature"]')
    consent_signature2.send_keys(row['First Name'])
    save_changes = web.find_element_by_xpath('//*[@id="save_consent_signature_button"]')
    save_changes.click()

    street = web.find_element_by_xpath('//*[@id="intake_personal_type_household_address_addressLine1"]')
    street.send_keys(row['Street Address'])

    time.sleep(1)

    postal_code = web.find_element_by_xpath('//*[@id="intake_personal_type_household_address_postcode"]')
    postal_code.send_keys(row['Postal / Zip Code'])

    martial_status = web.find_element_by_xpath(
        '//*[@id="intake_personal_type"]/div[2]/div[1]/div[8]/div/div/div/div/div[4]/div[1]')
    martial_status.click()

    housing_type = web.find_element_by_xpath(
        '//*[@id="intake_personal_type"]/div[3]/div[1]/div[2]/div/div/div/div/div[3]/div[3]')
    housing_type.click()

    referred_by = web.find_element_by_xpath('//*[@id="s2id_intake_personal_type_referredBy"]/a')
    referred_by.click()
    Referred = "Other (Specify)"
    referred_by2 = web.find_element_by_xpath('//*[@id="select2-drop"]/div/input')
    referred_by2.send_keys(Referred)
    referred_by2.send_keys(Keys.ENTER)
    Referred2 = "N/A"
    referred_by3 = web.find_element_by_xpath('//*[@id="intake_personal_type_referredByOther"]')
    referred_by3.send_keys(Referred2)

    ethnicity = web.find_element_by_xpath('//*[@id="intake_personal_type"]/div[11]/div/div/div/div/div[4]/div[2]')
    ethnicity.click()

    disability = web.find_element_by_xpath(
        '//*[@id="intake_personal_type"]/div[12]/div/div/div/div/div/div[2]/div[1]')
    disability.click()

    canadian_citizen = web.find_element_by_xpath(
        '//*[@id="intake_personal_type"]/div[13]/div/div/div/div/div/div[2]/div[1]')
    canadian_citizen.click()

    self_identify = web.find_element_by_xpath(
        '//*[@id="intake_personal_type"]/div[14]/div/div/div/div/div[3]/div[2]')
    self_identify.click()

    print("")
    print("")
    print("")
    continue2 = input("Do you wish to continue: ").lower()

# Child Adding or Complete Program
    if continue2 == "yes":
        main_2()
    elif continue2 == "no":
        final()
    elif continue2 == "exit":
        exit()

# where the code begins
main()