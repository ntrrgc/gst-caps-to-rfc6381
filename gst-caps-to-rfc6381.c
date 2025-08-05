#include <gst/gst.h>
#include <gst/pbutils/codec-utils.h>
#include <glib.h>

int
main (int   argc,
      char *argv[])
{
  gst_init (&argc, &argv);

  if (argc != 2) {
    g_printerr ("Usage: %s <caps-string>\n", argv[0]);
    return -1;
  }

  GstCaps* caps = gst_caps_from_string (argv[1]);
  if (!caps) {
    g_printerr("Failed to create caps.\n");
    return -1;
  }
  gchar* mime_codec = gst_codec_utils_caps_get_mime_codec (caps);
  if (!mime_codec) {
    g_printerr ("Could not create a MIME codec string.\n");
    return -1;
  }

  g_print ("%s\n", mime_codec);

  g_free (mime_codec);
  gst_caps_unref (caps);
  return 0;
}
