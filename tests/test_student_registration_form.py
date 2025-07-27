import os
import pytest
from selene import browser, have

def test_student_registration_forme():
 browser.open('https://demoqa.com/automation-practice-form')

 # заполнение Name: поля First Name и Last Name
 browser.element('[id="firstName"]').type('Anna')
 browser.element('[id="lastName"]').type('Kostina')

 # заполнение поля Email
 browser.element('[id="userEmail"]').type('111name@example.com')

 # выбор Gender
 browser.element('label[for="gender-radio-2"]').click()

 # заполнение поля Mobile
 browser.element('[id="userNumber"]').type('8788888888')

 # выбор Date of Birth кликом из календаря
 browser.element('[id="dateOfBirthInput"]').click()
 browser.element('button[aria-label="Previous Month"]').click()
 browser.element('[aria-label="Choose Wednesday, June 18th, 2025"]').click()

 # выбор Date of Birth из выпадающих списков в календаре
 # browser.element('[id="dateOfBirthInput"]').click()
 # browser.element('[class="react-datepicker__year-select"]').click()
 # browser.element('[value="1992"]').click()
 # browser.element('[class="react-datepicker__month-select"]').click()
 # browser.element('[value="3"]').click()

# выбор Subjects
 browser.element('#subjectsInput').type('co')
 browser.element('.subjects-auto-complete__option').click()

# выбор Hobbies
 browser.element('label[for="hobbies-checkbox-2"]').click()
 browser.element('label[for="hobbies-checkbox-3"]').click()

# добавление Picture
 browser.element('#uploadPicture').send_keys(os.path.abspath('test.jpg'))

# заполнение поля Current Address
 browser.element('[id="currentAddress"]').type('Moscow')

# заполнение State and City: выбор State, затем City
 browser.element('[id="state"]').click()
 browser.element('div[class*="option"]').click()
 browser.element('[id="city"]').click()
 browser.element('div[class*="option"]').click()

 # отправка формы
 browser.element('[id="submit"]').click()

 # проверка формы "Thanks for submitting the form"
 browser.element('[class="modal-content"]').should(have.text('Thanks for submitting the form'))
 browser.element('.table').should(have.text('Anna Kostina'))
 browser.element('.table').should(have.text('111name@example.com'))
 browser.element('.table').should(have.text('Female'))
 browser.element('.table').should(have.text('8788888888'))
 browser.element('.table').should(have.text('18 June,2025'))
 browser.element('.table').should(have.text('Computer Science'))
 browser.element('.table').should(have.text('Reading, Music'))
 browser.element('.table').should(have.text('test.jpg'))
 browser.element('.table').should(have.text('Moscow'))
 browser.element('.table').should(have.text('NCR Delhi'))