#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: qr.py

import qrcode


def main():
    image = qrcode.make("https://127.0.0.1:8000")
    image.save("qr.png")


if __name__ == "__main__":
    # If this script is run directly, call the main function
    main()
