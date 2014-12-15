from lettuce import *
from nose.tools import assert_equal, assert_in
from webtest import TestApp

from tallier.tallier import Tallier
from tallier_app import app, TALLIER



@step(u'')