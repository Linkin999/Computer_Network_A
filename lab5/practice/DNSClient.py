import dns.resolver
import sys
import dns.message
from dns import resolver,flags
from dns.flags import Flag




# See PyCharm help at https://www.jetbrains.com/help/pycharm/

if __name__ == "__main__":

    setRD=input("RD is set(y),RD is not set(n):")
    reso =dns.resolver.BaseResolver
    if setRD=="y":
        reso.set_flag(0x0100)
    elif setRD=="n":
        reso.set_flag(0x0000)
    else:
        reso.set_flag(None)

    domain = sys.argv[1]
    queryType = sys.argv[2]
    resol=dns.resolver.Resolver(reso)
    q = resol.resolve(qname=domain, rdtype=queryType, raise_on_no_answer=False)

    try:

        print('Answer:', q.response)
        print()
        print('Who send the server', q.nameserver)
        print()
        print('Port Number', q.port)
        print()
        print('Is from authority name server?', 'AUTHORITY' in str(q.response))
    except dns.resolver.NoAnswer as na:
        print('This request contains no content')
