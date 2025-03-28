#!/usr/bin/env python3

import connexion

from josch83_api import encoder


def main():
    app = connexion.App('josch83_api', specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'ferris.ai ipt JSC &amp; TZI'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
