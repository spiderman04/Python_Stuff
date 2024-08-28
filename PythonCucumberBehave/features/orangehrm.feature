# To use parameters use the "" quotes for the variable replacement
# and then use {} in the implementation code in Python 'def'

# Use the "<> symbols in the Example keyword section for varaibles.

# use the @Smoke and @regression tags to better define the test at ruintime
# syntax for comamnd line is --tags=smoke, regression or ~smoke or testTable

# The 'Table' element is useful for test data for a specific testcase

# The 'Background' section is a common set of steps to execute. It can contain
# one or more Given steps.

@orangeTests
Feature: OrangeHRM Logo

    Background:
        Given Launch Firefox Browser

    Scenario: Logo presence on OrangeHRM home page
        When open orange hrm homepage
        Then verify logo present on page
        And close browser
