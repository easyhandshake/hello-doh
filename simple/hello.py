# coding=utf-8


# network.trr.mode   3
# network.trr.uri   https://easyhandshake.com:8053/dns-query
# network.trr.bootstrapAddress   165.22.151.242


# https://easyhandshake.com:8053/dns-query?name=rough&type=A

import client

print(client.query("rough", "A", server="easyhandshake.com:8053"))
