
Feature: OrangeHRM Login

    Background:
        Given I launch Firefox Browser

    Scenario Outline: Login to OrangeHRM with valid parameters
        When I open orange HRM homepage
        And Enter username "<username>" and password "<password>"
        And Click on login button
        Then User must successfully login to the Dashboard page
        Examples:
            | username | password |
            | Admin | admin123 |
            | admin1234 | admin |

    Scenario Outline: Login to OrangeHRM with valid parameters
        When I open orange HRM homepage
        And Enter username "<username>" and password "<password>"
        And Click on login button
        Then User must successfully login to the Dashboard page
        Examples:
            | username | password |
            | Admin | admin123 |