#!/usr/bin/env python3

import connexion

from jsctzi_api import encoder


def main():
    app = connexion.App('jsctzi_api', specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'ferris.ai None ipt JSC &amp; TZI'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
