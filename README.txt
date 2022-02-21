============
    ta2
============

Team assignment tool. Reads a CSV file
from resources/ and translates the team
assignments therein to entries in Canvas.
Currently designed to split users into
group categories by their tutorial.

To use, do

`pip install -r requirements.txt`

Then, in a python interpreter,

```
import vibes
vibes.vibes()
```

A few notes:
- you'll need to throw an API key
	for canvas into authentication.py
- you'll need to populate
	resources/team_assignment.csv

The algorithm will run and then you'll
have a list of "messed up teams" - these
are teams with folks who've since dropped
the class. You may need to manually edit
these if teams of 2 or fewer pop up.

