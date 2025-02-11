def subdomainVisitCount(ar):
    hm = {}
    for i in range(len(ar)):
        d = ar[i].split()
        domains = d[1].split(".")
        p = len(domains)
        for j in range(p-1, -1, -1):
            if tuple(domains[p - j-1:]) not in hm:
                hm[tuple(domains[p - j-1:])] = int(d[0])
            else:
                hm[tuple(domains[p - j-1:])] += int(d[0])
    res = []
    for j in hm:
        res.append(str(hm[j])+ " " + ".".join(j))
    return res

print(subdomainVisitCount(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))