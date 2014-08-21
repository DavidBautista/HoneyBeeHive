

SCORE_CHOICES = zip(range(1, 10), range(1, 10))

PROJECT_METODOLOGES = (
    (u'Scrum', u'Scrum'),
    (u'Traditional', u'Traditional'),
    (u'Kanvas', u'Kanvas'),
)

WORKERS_PERMISSIONS = (
    (1, u'Read'),
    (2, u'Write'),
    (3, u'Admin'),
)

TASKS_STATUS = (
    (1, u'Prepared'),
    (2, u'Working'),
    (3, u'Paused'),
    (4, u'Finished'),
)

# models.SmallIntegerField(choices=((1, '1960-1969'), 2, '1970 - 1970))