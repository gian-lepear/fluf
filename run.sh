#!/bin/bash

cd fluf
gunicorn fluf.wsgi —-log-file -
