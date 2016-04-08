#!/usr/bin/env python

import os

# Have to pass these variables in from Dockerfile or other method
evePort = os.environ['EVEPORT']
mongo = os.environ['MONGODB']
mongoPort = os.environ['MONGOPORT']

my_settings = {
	'MONGO_HOST': mongo,
	'MONGO_PORT': mongoPort,
	'RESOURCE_METHODS': ['GET','POST','DELETE'],
	'ITEM_METHODS': ['GET','PATCH','PUT','DELETE'],
        'DOMAIN': {  
			'walkupobjects': {
				'schema': {
					'objecttype': {
						'type': 'list',
						'allowed': ["golf"],
						'required': True
					},
					'objectname': {
						'type': 'string',
						'minlength': 1,
						'maxlength': 100,
						'required': True,
						'unique': True
					},
					'location': {
						'type': 'point',
						'required': True
					},
					'status': {
						'type': 'string',
						'minlength': 1,
						'maxlength': 10
					}
				}
			},
			'walkuplists': {
				'schema': {
					'object': {
						'type': 'objectid',
						'data_relations': {
							'resource': 'walkupobjects'
						}
					},
					'listdate': {
						'type': 'datetime'
					},
					'listmember': {'type': 'dict',
						'schema': {
							'customer': {
								'type': 'objectid',
								'data_relation': {
									'resource': 'walkupcustomers'
								}
							},
							'submitted': {'type': 'datetime'},
							'processed': {'type': 'datetime'},
							'status': {
								'type': 'list',
								'allowed': ["success","deleted","waiting"]
							}
						}
					}
				}
			},
			'walkupcustomers': {
				'schema': {
					'mobilenumber': {
						'type': 'number',
						'required': True
					}
				}
			}
		}
	}

from eve import Eve
app = Eve(settings=my_settings)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=evePort)
