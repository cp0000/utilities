#!/bin/bash
# cheng pei created by 20140327

from='zh-CN'
to='en'
wordData=$PWD/word.data

if [ ! -f $wordData ]; then
    echo "File not find, touch file: "$wordData
    touch $wordData
fi

if [ "$1" == "en" ];then
    from="en"
    to="zh-CN"
else
    from="zh-CN"
    to="en"
fi

url='http://translate.google.com/translate_a/t?client=t&text='$2'&hl='$from'&sl='$from'&tl='$to'&ie=UTF-8&oe=UTF-8&multires=1&prev=btn&ssel=0&tsel=0&sc=1'

# curl -s -A "Mozilla/5.0" $url\ | sed 's/\[\[\["\([^"]*\).*/\1/'


echo "$2">> $wordData
curl -s -A "Mozilla/5.0" $url\ | xargs echo >> $wordData
tail -1 $wordData
echo "">> $wordData


# Only for macosx
say $2 

