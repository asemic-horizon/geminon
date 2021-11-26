# geminon
This is a Python 3 script that converts between the Wordpress export format and GMI gemlogs.

It basically consists of some light glue code on top of `wpparser`, which handles the Wordpress export format, and `markdownify`, which gets rid of most markup.

To run, first have the dependencies ready

```
pip install wpparser markdownify
```

and then

```
python geminon.py your_export_file.xml
```
