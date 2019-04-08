################################################################################
# Generate Google Dorks by John Oberlin                                     [80]
################################################################################

# Input known info #############################################################
domain = "example.com"
first = "John"
last = "Doe"

# Find related emails ##########################################################
# Dork templates
templates = [
  "site:<domain> intext:(\"<first>\" \"<last>\" <e_hosts>)",
  "site:<domain> intext:(\"<first>\" \"<last>\" <e_hosts>) filetype:(csv | xls | xlsx)",
  "site:<domain> intext:(<e_hosts>)",
  "intext:\"<last>@<domain>\""
]

# Common email hosts list
e_hosts = ["@gmail.com", "@yahoo.com", "@aol.com", "@outlook.com",]
# Add particular domain as email host
e_hosts.append("@"+domain)
# Build dork string for email hosts
e_hosts_str = ""
for h in e_hosts:
  if e_hosts.index(h) == 0:
    e_hosts_str += "\""+h+"\""
  else:
    e_hosts_str += " | \""+h+"\""

# Build dorks from input and templates
dorks = []
for t in templates:
  dork = t
  dork = dork.replace("<domain>", domain)
  dork = dork.replace("<e_hosts>", e_hosts_str)
  dork = dork.replace("<first>", first)
  dork = dork.replace("<last>", last)
  # Encode dork URL option
  url_encoding = {  " ": "+",    "(": "%28",   ")": "%29",
                    "|": "%7C",  ":": "%3A",              }
  dork_url = dork
  for k, v in url_encoding.items():
    dork_url = dork_url.replace(k, v)
  dork_url = "https://www.google.com/search?q=" + dork_url
  # Build dork JSON-like dictionary
  dork_set = {}
  dork_set["dork"] = dork
  dork_set["dork_url"] = dork_url
  dorks.append(dork_set)

# Output
for dork_set in dorks:
  for k, v in dork_set.items():
    print(k+": "+v)
  print("\n")
