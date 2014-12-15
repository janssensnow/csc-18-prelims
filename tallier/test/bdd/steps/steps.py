from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp

from tallier.tallier import Tallier
from tallier_app import app, TALLIER



@step(u'Team 1 is a registered team')
def given_Team_1_is_a_registered_team(step):
    score = Score(Team 1, 0)