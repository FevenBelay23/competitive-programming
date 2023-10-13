class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def ipv4(query):
            ip = query.split('.')
            if len(ip) != 4:
                return False
            for i in ip:
                if not i:
                    return False
                if not i.isnumeric():
                    return False
                if not 0 <= int(i) <= 255:
                    return False
                if i[0] == '0' and len(i) > 1:
                    return False
            return True
        
        def ipv6(query):
            ip = query.split(':')
            if len(ip) != 8:
                return False
            for i in ip:
                if not i:
                    return False
                if not 1 <= len(i) <= 4:
                    return False
                if not all(j in '0123456789abcdefABCDEF' for j in i):
                    return False
            return True
            
        if '.' in queryIP and ipv4(queryIP):
            return 'IPv4'
        if ':' in queryIP and ipv6(queryIP):
            return 'IPv6'
        return 'Neither'
                
            
                
        
            
        