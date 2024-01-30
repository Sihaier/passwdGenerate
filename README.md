# passwdGenerate

Automatically generate passwords based on keywords



## How to Use?

```python
python main.py -h
```

usage: main.py [-h] [--min MIN] [--max MAX] [-k LIST [LIST ...]] [-o OUTPUT]

manual to this script

optional arguments:
  -h, --help            show this help message and exit
  --min MIN             min number for password length
  --max MAX             max number for password length
  -k LIST [LIST ...], --keys LIST [LIST ...]
                        Use these keys as an extension
  -o OUTPUT, --output OUTPUT
                        output filename



```python
python main.py -k microsoft abc admin
```

min number:  6
max number:  10
keys list:  ['microsoft', 'abc', 'admin']
output filename:  passwd.txt
success output password in your current dir path

## params

--min:  min password length

--max: max passwrd length

-o:  output filename
