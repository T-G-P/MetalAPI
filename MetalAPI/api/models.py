from django.db import models

class Band(models.Model):
    ma_id = models.BigIntegerField()
    name = models.TextField()
    url = models.URLField()
    country = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    lyrical_themes = models.CharField(max_length=200)
    formation_year = models.CharField(max_length=200)
    current_label = models.CharField(max_length=200)
    years_active = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    description = models.TextField()

class Release(models.Model):
    band = models.ForeignKey(Band)
    #name = models.CharField(max_length=200)
    name = models.TextField()
    notes = models.TextField()
    length = models.CharField(max_length=200)
    release_id = models.BigIntegerField()
    release_type = models.CharField(max_length=200)
    release_year = models.IntegerField()
    #release_category = models.CharField(max_length=200)

class BandLineup(models.Model):
    # Enumerable choices for lineup type.
    CURRENT = 'CR'
    LIVE = 'LI'
    PAST = 'PA'
    COMPLETE = 'CP'
    LINEUP_TYPES = (
        (CURRENT, 'current'),
        (LIVE, 'live'),
        (PAST, 'past'),
        (COMPLETE, 'complete'),
    )

    band = models.ForeignKey(Band)
    lineup_type = models.CharField(max_length=2, choices=LINEUP_TYPES)

class ReleaseLineup(models.Model):
    release = models.ForeignKey(Release)

# Make this generic later
class BandMusician(models.Model):
    lineup = models.ForeignKey(BandLineup)
    #name = models.CharField(max_length=200)
    name = models.TextField()
    #role = models.CharField(max_length=200)
    role = models.TextField()

# Make this generic later
class ReleaseMusician(models.Model):
    lineup = models.ForeignKey(ReleaseLineup)
    #name = models.CharField(max_length=200)
    name = models.TextField()
    #role = models.CharField(max_length=200)
    role = models.TextField()

class Song(models.Model):
    release = models.ForeignKey(Release)
    track_number = models.IntegerField()
    #name = models.CharField(max_length=200)
    name = models.TextField()
    length = models.CharField(max_length=200)
    lyrics = models.TextField()

class SimilarArtist(models.Model):
    band = models.ForeignKey(Band)
    #name = models.CharField(max_length=200)
    name = models.TextField()
    country = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    ma_id = models.BigIntegerField()

class RelatedLinks(models.Model):
    band = models.ForeignKey(Band)
    category = models.CharField(max_length=200)
    link_type = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
