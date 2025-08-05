#!/bin/bash
gcc -O0 -g -Wall gst-caps-to-rfc6381.c -o gst-caps-to-rfc6381 \
  $(pkg-config --cflags --libs gstreamer-1.0) \
  $(pkg-config --cflags --libs gstreamer-pbutils-1.0)
