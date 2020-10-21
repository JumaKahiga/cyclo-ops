"""
Database table schemas
"""

from cyclops.resources.models import db


class Cyclone(db.Model):
    """Cyclone schema. """

    id = db.Column(db.Integer(), primary_key=True)
    basin = db.Column(db.String(30))
    storm_url = db.Column(db.String(150))
    storm_identifier = db.Column(db.String(150))
    img_url = db.Column(db.String(150))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self
