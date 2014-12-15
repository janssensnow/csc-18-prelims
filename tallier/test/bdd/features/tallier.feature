Feature: Basket ball score tallier application to record
         and tally scores of a basketball game

         As a scorer I wish to tally scores of competing teams in a
         basketball game and update these scores when a player from
         a team scores

         Scenario: Get initial score
            Given I create team:
                | Team Name | Score |
                | Team 1    | 0     |

             And I visit the homepage
             When I enter the Team Name "Team 1"
             Then I see the Score "0"
