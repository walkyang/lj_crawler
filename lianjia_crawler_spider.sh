#!/bin/bash
. /etc/profile
. ~/.bash_profile
my_city=('sh' 'hz' 'su' 'wx' 'ks' 'nb' 'jx' 'sx' 'changzhou' 'zj' 'nj' 'xz' 'yc' 'hf')
my_array=('310000' '330100' '320500' '320200' '320583' '330200' '330400' '330600' '320400' '321100' '320100' '320300' '320900' '340100')
for m_id in $(seq 0 `expr ${#my_array[*]} - 1`)
do
cd /home/lianjia_crawler
scrapy crawl lianjia_crawler_spider -L INFO -a city_id=${my_array[$m_id]} -a city_code=${my_city[$m_id]}
done