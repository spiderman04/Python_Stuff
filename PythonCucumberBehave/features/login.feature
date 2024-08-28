# To use parameters use the "" quotes for the variable replacement
# and then use {} in the implementation code in Python 'def'

# Use the "<> symbols in the Example keyword section for varaibles.

# use the @Smoke and @regression tags to better define the test at ruintime
# syntax for comamnd line is --tags=smoke, regression or ~smoke or testTable

# The 'Table' element is useful for test data for a specific testcase

# The 'Background' section is a common set of steps to execute. It can contain
# one or more Given steps.

Feature: Login functionality for NewTours Application

    Background:
        Given Open Browser

    @smoke
    Scenario: Valid user name and password
        # Given Open Browser
        # When Providing valid "mercury" and "mercury"
        When Providing valid "username" and "password"
        Then Verify Home Page
        And Logoff and close browser

    @regression
    Scenario Outline:
        # Given Open Browser
        When Providing valid "<username>" and "<password>"
        Then Verify Success Message
        And Logoff and close browser
        Examples:
            | username | password |
            | mercury | mercury |
            | abcdefgh | junkjunk |

@testTable
Scenario: Testing table formats
        # Given Open Browser
        When Verify login by using below query
            | username | password |
            | mercury | mercury |
        Then Verify title on page
        And Logoff and close browser

