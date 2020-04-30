#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension


def main():
    setup(name="matrix",
          version="1.0.0",
          description="Matmul C extension",
          ext_modules=[Extension("matrix", ["test.c"])])

if __name__ == "__main__":
    main()
    