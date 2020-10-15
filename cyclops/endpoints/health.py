"""
Service status endpoint
"""
from flask import Blueprint
from flask_apispec import marshal_with
from marshmallow import Schema, fields

health = Blueprint('health', __name__)


class HealthSchema(Schema):
    service_status = fields.String(description='the service health status')


@health.route('/api/health')
@marshal_with(HealthSchema, code=200)
def get():
    """
    Returns service status.
    """

    return {'service_status': 'healthy'}
