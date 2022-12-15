import requests 
import time 
import sys 

BRANCH_NAME = 'dev-{}'.format(sys.argv[1])
GIT_BRANCH_REF = sys.argv[2]
REPO_API_URL = 'https://packagist.org/packages/PargoPoints/plugin-magento.json'

def get_package_version():
  print ("Git Ref: {}".format(GIT_BRANCH_REF))
  version_data = requests.get(REPO_API_URL)
  version_json = (version_data.json())
  source_ref = 'a'
  dist_ref = 'b'
  while dist_ref != GIT_BRANCH_REF and source_ref != GIT_BRANCH_REF:
    try:
        print ("Packagist Source Ref: {}, Packagist Dist Ref: {}".format(source_ref,dist_ref))
        source_ref = (version_json['package']['versions'][BRANCH_NAME]['source']['reference'])
        dist_ref = (version_json['package']['versions'][BRANCH_NAME]['dist']['reference'])
        print ("Checking branch refs...")
        time.sleep(5)
    except Exception as e:
        print ("Unable to find packagist info {}".format(e))

  print ("Package source and dist match")

get_package_version()