# F2B64AndBack

## Inspired From
[This Gist](https://gist.github.com/amoghmadan/17eeb81824b00f4010ba1ef07fe22740) 

## Installing requirements
```bash
pip install -r requirements.txt
```

## Usage
File to Base64 String.
 ```bash
python f2b64_and_back.py 0 path_to_file > base64.txt 
```

Base64 String(Stored in a file) to File.
```bash
python f2b64_and_back.py 1 path_to_base64_string_file.txt -of CustomFileName
```

## Help
```bash
python f2b64_and_back.py -h
```