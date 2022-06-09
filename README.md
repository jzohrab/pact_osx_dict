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
LookupModule = myplugins.pact_osx_dict.osxdict
```

## Development

Code from requirements.txt vendored with:

```
python -m pip install -r requirements.txt --target=./vendor
```