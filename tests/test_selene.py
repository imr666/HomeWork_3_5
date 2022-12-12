import os.path
from selene.support.shared import browser
from selene import have

picture = os.path.abspath(os.path.join(os.path.dirname(__file__), 'resources', 'screen.png'))

def test_demoqa():
    #name, gender, contacts
    browser.element('#firstName').type('Alexey')
    browser.element('[id="lastName"]').type('Filin')
    browser.element('[id="userEmail"]').type('rsimr3@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type('9200560797')
    #date of birth
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('[class="react-datepicker__month-select"]').click()
    browser.element('[value="0"]').click()
    browser.element('[class="react-datepicker__year-select"]').click()
    browser.element('[value="1999"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--019"]').click()
    #subkects, hobbies
    browser.element('[id="subjectsInput"]').click().type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    #picture
    browser.element('#uploadPicture').send_keys(picture)
    #adress
    browser.element('[id="currentAddress"]').type('none')
    browser.element('[id="react-select-3-input"]').type('NCR').press_enter()
    browser.element('[id="react-select-4-input"]').type('Delhi').press_enter()
    #submit
    browser.element('[id="submit"]').press_enter()
    browser.element('[class="table-responsive"]').should(have.text(
    'Alexey'
    and 'Filin'
    and 'rsimr3@gmail.com'
    and 'Male'
    and '9200560797'
    and '19 January,1999'
    and 'Maths'
    and 'Sports'
    and 'screen.png'
    and 'none'
    and 'NCR'
    and 'Delhi'))