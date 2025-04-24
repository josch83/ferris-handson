#!/usr/bin/env python3

import connexion

from magdemo_api import encoder


def main():
    app = connexion.App('magdemo_api', specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'ferris.ai Ferris Demo Project for MAG Hands On'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
