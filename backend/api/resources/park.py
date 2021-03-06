from flask import abort
from flask_restplus import Resource

from server.instance import server, db
from models.park import park
from .dao import (get_all, get_by_id, create_single_by_id,
                  update_by_id, delete_by_attr)

api = server.api

park_ns = api.namespace('parks', description='park related endpoints')


@park_ns.route('')
class ParkList(Resource):
    @api.marshal_list_with(park)
    def get(self):
        """Retrieve all parks."""
        return get_all('park', db)

    @api.expect(park, validate=True)
    @api.marshal_with(park)
    def post(self):
        """Create a new park."""
        attrs = ['p_name', 'p_polygon', 'mid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return create_single_by_id(vals, attrs, 'pid', 'park', db)
        except Exception as e:
            abort(400, str(e))


@park_ns.route('/<int:pid>')
class Park(Resource):
    @api.marshal_with(park)
    @api.response(404, 'Not Found')
    def get(self, pid):
        """Retrieve a specific park."""
        record = get_by_id(pid, 'pid', 'park', db)
        return record if record else ('Not Found', 404)

    def delete(self, pid):
        """Delete a specific park."""
        delete_by_attr([pid], ['pid'], 'park', db)

    @api.expect(park, validate=True)
    @api.marshal_with(park)
    def put(self, pid):
        """Update a specific park."""
        attrs = ['p_name', 'p_polygon', 'mid']
        vals = list(map(lambda attr: api.payload[attr], attrs))
        try:
            return update_by_id(vals, attrs, pid, 'pid', 'park', db)
        except Exception as e:
            abort(400, str(e))
