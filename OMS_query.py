## From lxplus
## https://gitlab.cern.ch/cmsoms/oms-api-client
## https://gitlab.cern.ch/cms-tsg-fog/ratemon/-/tree/master/ratemon

from omsapi import OMSAPI

omsapi = OMSAPI("https://cmsoms.cern.ch/agg/api", "v1", cert_verify=False)
omsapi.auth_krb()

# Create a query
q = omsapi.query("runs")

# Chain filters
q.paginate(page=1, per_page=1).sort("run_number", asc=False)

# Execute query & fetch data
response = q.data()

# Display JSON data
print(response.json())
