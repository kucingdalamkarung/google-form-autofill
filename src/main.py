import random
from time import sleep

from selenium import webdriver

from utils.generator import Generator

BASE_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSelb6KywLQcbCXyqcKvjM4P0BictjV6wB7UW-NJ7fslYr4E8g/viewform'


def main():
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    browser = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=option)
    browser.get(BASE_URL)

    # first page of google form
    radio_bersedia = browser.find_element_by_class_name('freebirdFormviewerComponentsQuestionRadioChoicesContainer')
    next_button = browser.find_element_by_class_name('appsMaterialWizButtonPaperbuttonLabel')

    radio_bersedia.click()
    # click next button to go to next page
    next_button.click()
    # end first page of google form

    # beginning of second page
    textInputField = browser.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
    namaInput = textInputField[0]
    usiaInput = textInputField[1]
    perguruanTinggiInput = textInputField[2]
    semesterInput = textInputField[3]
    daerahInput = textInputField[4]
    ipkInput = textInputField[5]

    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    radioLaki = radiobuttons[0]
    radioPerempuan = radiobuttons[1]

    namaInput.send_keys(Generator.generateInitialName())
    usiaInput.send_keys(Generator.generateAge(18, 35))
    perguruanTinggiInput.send_keys('-')
    semesterInput.send_keys(Generator.generateSemester())
    daerahInput.send_keys('-')
    ipkInput.send_keys(Generator.generateIPK())

    randomGender = random.randint(1, 2)
    if randomGender == 1:
        radioLaki.click()
    elif randomGender == 2:
        radioPerempuan.click()

    check_count = random.randint(1, 3)

    # 10 checkboxes
    # checkboxes for platform kuliah
    checkboxes = browser.find_elements_by_class_name("quantumWizTogglePapercheckboxInnerBox")
    for i in range(check_count):
        randomCheck = random.randint(1, 8)
        checkboxes[randomCheck].click()

    # goto next page
    buttons = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonContent')
    buttons[1].click()
    # end of second page

    # beginning of third page
    # answer the question
    radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    answers = Generator.generateAnswer(43)
    for i in range(len(answers)):
        radiobuttons[answers[i]].click()

    # go to next page
    buttons = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonContent')
    buttons[1].click()
    # end of third page

    # beginning of fourth page
    # answer the question
    radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    answers = Generator.generateAnswer(43)
    for i in range(len(answers)):
        radiobuttons[answers[i]].click()

    buttons = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonContent')
    buttons[1].click()
    # end of fourth page

    # beginning of 5th page
    radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    answers = Generator.generateAnswer(43)
    for i in range(len(answers)):
        radiobuttons[answers[i]].click()

    buttons = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonContent')
    buttons[1].click()
    # end of 5th page

    # beginning of 6th page
    radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    answers = Generator.generateAnswer(43)
    for i in range(len(answers)):
        radiobuttons[answers[i]].click()

    buttons = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonContent')
    buttons[1].click()
    # end of 6th page

    # beginning of 7th page
    radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
    answers = Generator.generateAnswer2(9)
    print(answers)
    for i in range(len(answers)):
        radiobuttons[answers[i]].click()
    #
    buttons = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonLabel')
    buttons[-1].click()
    # end of 7th page

    # beginning of 8th page
    radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    answers = Generator.generateAnswer(24)
    for i in range(len(answers)):
        radiobuttons[answers[i]].click()

    buttons = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonContent')
    buttons[1].click()
    # end of 8th page

    # beginning of 9th page
    radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    answers = Generator.generateAnswer3(10)
    for i in range(len(answers)):
        radiobuttons[answers[i]].click()

    buttons = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonContent')
    buttons[1].click()
    # end of 9th page

    # beginning of 10th page
    radiobuttons = browser.find_elements_by_class_name("appsMaterialWizToggleRadiogroupOffRadio")
    answers = Generator.generateAnswer3(20)
    for i in range(len(answers)):
        radiobuttons[answers[i]].click()

    buttons = browser.find_elements_by_class_name('appsMaterialWizButtonPaperbuttonContent')
    buttons[1].click()
    # end of 10th page

    # send the answer

    sleep(100000)


if __name__ == "__main__":
    main()
