# Pact dictionary wrapper for OSX dictionary

## Usage in Pact

To use this as a Pact plugin:

### Get the code:

1. Create a new directory, `pact/myplugins/pact_osx_dict`
2. Download the zip file for this project from GitHub
3. Move the files from the unzipped file into the new `pact_osx_dict` folder

### Configure Pact

In the '[Pact]' section in your config.ini file, set

```
LookupModule = myplugins.pact_osx_dict.builtin
```

or

```
LookupModule = myplugins.pact_osx_dict.osxdict
```

Note: This was a proof-of-concept, mainly ... it uses the `macdict` python library to call the dictionary app, but the internal Apple library for the dict lookup doesn't seem to behave well (e.g. it only returns partial results).


## Development

Code from requirements.txt vendored with:

```
python -m pip install -r requirements.txt --target=./vendor
```