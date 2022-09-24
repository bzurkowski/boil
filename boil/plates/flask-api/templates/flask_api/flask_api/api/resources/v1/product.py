from flask_restplus import Namespace, Resource, fields

api = Namespace('products', description='Products API')

product = api.model('Product', {
    'id': fields.String,
    'name': fields.String,
    'price': fields.Integer
})


@api.route('/')
class Graph(Resource):
    @api.doc('get_products')
    @api.marshal_with(product)
    def get(self):
        '''List all products'''
        products = [
            {'id': 'myprod1',
             'name': 'myproduct1',
             'price': 120},
            {'id': 'myprod2',
             'name': 'myproduct2',
             'price': 150},
            {'id': 'myprod3',
             'name': 'myproduct3',
             'price': 20}
        ]
        return products
