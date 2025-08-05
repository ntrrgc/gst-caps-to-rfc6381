# MIME codec string (RFC6381) from GStreamer caps

Minimal programs that parse caps and calls `gst_codec_utils_caps_get_mime_codec()` on them.

Two functionally identical versions are available, one in C and one in Python.

## C version

Requirements:

 * gcc
 * bash
 * GStreamer

Building:

```
$ ./make.sh
```

Usage:

```
$ ./gst-caps-to-rfc6381 "video/x-h264, stream-format=(string)avc, alignment=(string)au, level=(string)1.1, profile=(string)high, codec_data=(buffer)0164000bffe1001d6764000bace40507ec05a830082d280000030008000003003478a1489001000568ebecb22cfdf8f800, width=(int)320, height=(int)240, framerate=(fraction)5/2, pixel-aspect-ratio=(fraction)1/1, colorimetry=(string)2:4:5:4"
avc1.64000B
```

## Python version

Requirements:

 * Python3
 * Python GObject Introspection
 * GStreamer with GObject introspection files (e.g. `/usr/lib64/girepository-1.0/GstPbutils-1.0.typelib`)

Usage:

```
$ ./gst-caps-to-rfc6381 "video/x-h264, stream-format=(string)avc, alignment=(string)au, level=(string)1.1, profile=(string)high, codec_data=(buffer)0164000bffe1001d6764000bace40507ec05a830082d280000030008000003003478a1489001000568ebecb22cfdf8f800, width=(int)320, height=(int)240, framerate=(fraction)5/2, pixel-aspect-ratio=(fraction)1/1, colorimetry=(string)2:4:5:4"
avc1.64000B
```