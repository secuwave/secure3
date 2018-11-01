# Running Script 1
## 2. Linux Shell
### 2.2 monitor

```bash
#! /bin/bash

while [ 1 ]
do
    date
    netstat -an | grep 5601
    vmstat
    echo -------------------
    sleep 3
done
```
