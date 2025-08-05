#!/usr/bin/env python3
import gi
import sys
from argparse import ArgumentParser
gi.require_version('Gst', '1.0')
gi.require_version('GstPbutils', '1.0')
gi.require_version('GLib', '2.0')
from gi.repository import GLib, Gst, GstPbutils # type: ignore

def main():
    parser = ArgumentParser()
    parser.add_argument("caps_string")

    args = parser.parse_args()

    Gst.init(sys.argv)
    caps = Gst.Caps.from_string(args.caps_string)
    if not caps:
        print("Failed to create caps.", file=sys.stderr)
        raise SystemExit(-1)
    mime_codec = GstPbutils.codec_utils_caps_get_mime_codec(caps)
    if not mime_codec:
        print("Could not create a MIME codec string.", file=sys.stderr)
        raise SystemExit(-1)
    print(mime_codec)

if __name__ == "__main__":
    main()
