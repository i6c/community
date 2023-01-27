# Copyright (C) 2012,2015 Claudio "nex" Guarnieri (@botherder), Optiv, Inc. (brad.spengler@optiv.com)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from lib.cuckoo.common.abstracts import Signature

dns_indicators = (
    "2ip.ru",
    "2ip.tools",
    "aboutmyip.com",
    "address.works",
    "api.ipify.org",
    "api.ipstack.com",
    "api.wipmania.com",
    "bearsmyip.com",
    "bot.whatismyipaddress.com",
    "check-my-ip.net",
    "checkip-waw.dyndns.com",
    "checkip.amazonaws.com",
    "checkip.dns.he.net",
    "checkip.dyndns.com",
    "checkip.dyndns.es",
    "checkip.dyndns.org",
    "checkip.narak.com",
    "checkmyip.com",
    "cmyip.com",
    "cmyip.net",
    "crymyip.com",
    "curlmyip.com",
    "curlmyip.net",
    "dawhois.com",
    "db-ip.com",
    "dnswatch.info",
    "dpool.sina.com.cn",
    "e-localizaip.com",
    "eth0.me",
    "extreme-ip-lookup.com",
    "findmyip.org",
    "findmyipaddress.com",
    "formyip.com",
    "freegeoip.app",
    "freegeoip.net",
    "free.ipwhois.io",
    "geodatatool.com",
    "geoip.co.uk",
    "geoip.vmn.net",
    "geoiptool.com",
    "get-myip.com",
    "getmyip.co.uk",
    "getmyip.org",
    "hostip.info",
    "icanhazip.com",
    "ident.me",
    "ifcfg.me",
    "ifconfig.co",
    "ifconfig.me",
    "ilmioip.it",
    "indirizzo-ip.com",
    "inet-ip.info",
    "ip-1.com",
    "ip-addr.es",
    "ip-address.cc",
    "ip-address.ru",
    "ip-adress.com",
    "ip-adress.eu",
    "ip-api.com",
    "ip-check.info",
    "ip-detect.net",
    "ip-info.ff.avast.com",
    "ip-info.org",
    "ip-info.xyz",
    "ip-ping.ru",
    "ip-score.com",
    "ip-secrets.com",
    "ip-tracker.org",
    "ip-who-is.com",
    "ip-whois.net",
    "ip.24.pl",
    "ip.amulex.com",
    "ip.anysrc.net",
    "ip.cctv.pk",
    "ip.chinaz.com",
    "ip.cn",
    "ip.my-proxy.com",
    "ip.samuraj-cz.com",
    "ip.taobao.com",
    "ip.tool.la",
    "ip.tyk.nu",
    "ip.webmasterhome.cn",
    "ip.xss.ru",
    "ip138.com",
    "ip2location.com",
    "ip2nation.com",
    "ip4.me",
    "ip4.telize.com",
    "ipaddress.com",
    "ipaddress.org",
    "ipaddresscheck.com",
    "ipapi.co",
    "ipchecker.info",
    "ipchicken.com",
    "ipecho.net",
    "ipify.org",
    "ipinfo.info",
    "ipinfo.io",
    "ipinfodb.com",
    "ipleak.net",
    "iplocation.com",
    "iplocation.net",
    "iplogger.org",
    "iplogger.ru",
    "ipmonkey.com",
    "iptrackeronline.com",
    "ipv4bot.whatismyipaddress.com",
    "ipv6-test.com",
    "ipv6bot.whatismyipaddress.com",
    "keliweb.it/mioip.php",
    "l2.io",
    "localizaip.com.br",
    "meip.eu",
    "meuip.net.br",
    "mio-ip.it",
    "mioip.biz",
    "mioip.ch",
    "mioip.info",
    "mioip.it",
    "mioip.org",
    "mioip.win",
    "moanmyip.com",
    "mon-ip.com",
    "my-ip-address.net",
    "mycamip.com",
    "myexternalip.com",
    "myglobalip.com",
    "myip.am",
    "myip.by",
    "myip.cc",
    "myip.cf",
    "myip.ch",
    "myip.cn",
    "myip.co.il",
    "myip.co.nz",
    "myip.com.br",
    "myip.com.tw",
    "myip.com.ua",
    "myip.cz",
    "myip.dk",
    "myip.dnsdynamic.org",
    "myip.dnsomatic.com",
    "myip.dramor.net",
    "myip.easylife.tw",
    "myip.es",
    "myip.eu",
    "myip.fi",
    "myip.gr",
    "myip.heltech.se",
    "myip.ht",
    "myip.info",
    "myip.io",
    "myip.is",
    "myip.israel.net",
    "myip.jacware.com",
    "myip.knet.ca",
    "myip.kz",
    "myip.ma",
    "myip.ms",
    "myip.mudfish.net",
    "myip.mysau.com.au",
    "myip.net",
    "myip.nl",
    "myip.nmonitoring.com",
    "myip.northstate.net",
    "myip.nu",
    "myip.opendns.com",
    "myip.ozymo.com",
    "myip.report",
    "myip.rs.sr",
    "myip.ru",
    "myip.sdu.dk",
    "myip.se",
    "myip.shorty.org",
    "myip.surfeasy.com",
    "myip.telespex.com",
    "myip.tk",
    "myip.tw",
    "myip.ua.edu",
    "myip.uconn.edu",
    "myip.v6shell.org",
    "myip.zone",
    "myipaddress.com",
    "myipinfo.net",
    "myipnow.com",
    "myipnumber.com",
    "myiponline.com",
    "mylocation.org",
    "readip.info",
    "shmyip.com",
    "show-ip.com",
    "show-my-ip.de",
    "showip.net",
    "showipinfo.net",
    "showips.com/api/geoip/",
    "showmemyip.com",
    "showmyip.co.uk",
    "showmyip.com",
    "showmyip.com.ar",
    "showmyip.gr",
    "showmyipaddress.com",
    "showmyipaddress.eu",
    "showmyipnow.com",
    "smart-ip.net",
    "tell-my-ip.com",
    "tinytools.nu",
    "tracemyip.com",
    "tracemyip.org",
    "trackip.net",
    "ultratools.com",
    "utrace.de",
    "v4.ident.me",
    "v6.ident.me",
    "vermiip.es",
    "vinflag.com",
    "whatismybrowser.com",
    "whatismyip.akamai.com",
    "whatismyip.ca",
    "whatismyip.com",
    "whatismyip.com.br",
    "whatismyip.everdot.org",
    "whatismyip.li",
    "whatismyip.net",
    "whatismyip.org",
    "whatismyipaddress.com",
    "whatismypublicip.com",
    "whatmyip.us",
    "whats-my-ip-address.org",
    "whatsmyip.ie",
    "whatsmyip.net",
    "whatsmyip.org",
    "whatsmyip.us",
    "whatsmyipaddress.com",
    "whatsmyipaddress.net",
    "whereisip.net",
    "whoer.net",
    "whois.pconline.com.cn",
    "wtfismyip.com",
    "www.ip.cn",
    "xmyip.com",
    "yougetsignal.com",
    "youip.net",
    "your-ip-address.com",
    "yourip.us",
    "geoplugin.net",
    "2ip.ua",
    "api.ip.sb",
    # public stun server list, from http://olegh.ftp.sh/public-stun.txt (could make this a feed I suppose)
    # all servers not matching our generic stun[0-9]?.* pattern below
    "iphone-stun.strato-iphone.de",
    "numb.viagenie.ca",
    "s1.taraba.net",
    "s2.taraba.net",
    "stunserver.org",
)

ip_indicators = ("23.21.150.121",)


class CheckIP(Signature):
    name = "recon_checkip"
    description = "Looks up the external IP address"
    severity = 2
    categories = ["network", "discovery"]
    authors = ["nex", "Optiv", "bartblaze"]
    minimum = "1.2"

    def run(self):

        found_matches = False
        for indicator in dns_indicators:
            if self.check_domain(pattern=indicator):
                self.data.append({"domain": indicator})
                found_matches = True
        matches = self.check_domain(pattern="^stun[0-9]?\..*", regex=True, all=True)
        if matches:
            found_matches = True
            for match in matches:
                self.data.append({"domain": match})

        for indicator in ip_indicators:
            if self.check_ip(pattern=indicator):
                self.data.append({"ip": indicator})
                found_matches = True

        return found_matches
