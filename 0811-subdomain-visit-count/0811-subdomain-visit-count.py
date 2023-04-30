class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain = {}
        for i in cpdomains:
            count, d = i.split()
            count = int(count)
            subdomains = d.split('.')
            for j in range(len(subdomains)):
                subdomain = '.'.join(subdomains[j:])
                if subdomain not in domain:
                    domain[subdomain] = 0
                domain[subdomain] += count
        result = []
        for d, count in domain.items():
            result.append(str(count) + " " + d)
        return result