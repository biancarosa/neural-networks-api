from flask import jsonify

class JSONResponseBuilder(object):

    @staticmethod
    def build_response(**kwargs):
        response = {}
        response['data'] = kwargs.get('data', [])
        response['success'] = kwargs.get('success', True)
        response['messages'] = kwargs.get('messages', [])
        return jsonify(response)
