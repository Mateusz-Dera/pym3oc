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

## Installation for Ubuntu 22.04
```sh
sudo apt-get install -y python3-pydub
cd /tmp
git clone https://github.com/Mateusz-Dera/pym3oc.git
sudo cp /tmp/pym3oc/pym3oc /bin
sudo chmod +x /bin/pym3oc
pym3oc -v
```

## Example of use
```sh
python3 pym3oc.py -i ~/file.mp3 -o ~/file.ogg -b 128
python3 pym3oc.py --input ~/file.mp3 -output ~/file.ogg
```
