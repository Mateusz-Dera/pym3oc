# pym3oc
## Info:
- Simple python3 mp3 to ogg file converter

## Usage:
|Short|Long|Description|
|---|---|---|
|-v|--version|Show version|
|-h|--help|Show help|
|-b|--bitrate|Bitrate|
|-i|--input|Input file|
|-o|--output|Output file|

Default bitrate is 128k

## Requirements for Ubuntu 22.04
```sh
sudo apt-get install -y python3-pydub
```

## Example of use
```sh
pym3oc -i ~/file.mp3 -o ~/file.ogg -b 128
pym3oc --input ~/file.mp3 -output ~/file.ogg
```
