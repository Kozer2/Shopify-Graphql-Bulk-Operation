import requests
import pandas as pd

# Runtime notes: ~8000 objects takes ~30 secs, ~65000 takes several minutes, 150k+ takes 10+ minutes
shop = 'YOUR SHOP NAME HERE' # Shop is what your shop is called in your homepage URL. EG. Shop called MyShop would be myshop.myshopify.com. Shop name = myshop
token = 'YOUR API PASSWORD HERE' # Token is the API Password
def getCustomerInfo():
    headers = {
        'Content-Type': 'application/json', # Need to tell the API that it is application/json 
        'X-Shopify-Access-Token': f'{token}',
    }
    # In the data variable we tell the Graphql request what exactly we want. In this case we want all the customers IDs, Emails, and the phone which can be located as a normal field or under the address property. Resources: https://shopify.dev/api/admin/graphql/reference
    data = ''' 
    mutation {
        bulkOperationRunQuery(
            query: """
            {
                customers(first: 10){
                    edges {
                        node {
                            id
                            email
                            phone
                            addresses {
                                phone
                            } 
                        }
                    }
                }
            }
            """
        ) {
            bulkOperation {
                id
                status
            }
            userErrors {
                field
                message
            }
        }
    }
'''
    response = requests.post(f'https://{shop}.myshopify.com/admin/api/2019-07/graphql.json', json={'query': data}, headers=headers)
    return response.json()

def checkBulkStatus():
    headers = {
        'Content-Type': 'application/json',  # Need to tell the API that it is application/json 
        'X-Shopify-Access-Token': f'{token}',
    }
    data = '''
    query {
        currentBulkOperation {
        id
        status
        errorCode
        createdAt
        completedAt
        objectCount
        fileSize
        url
        partialDataUrl
        }
    }
        '''
    response = requests.post(f'https://{shop}.myshopify.com/admin/api/2019-07/graphql.json', json={'query': data}, headers=headers)
    return response.json()
# Below here we are beginning our bulk operation with the Initializer, it will come back as a dict with a length of 2. We print off the ID and the status at the end. 
bulkOperationInitializer = (getCustomerInfo())
print(bulkOperationInitializer['data']['bulkOperationRunQuery'])

# Here we are running the check of our bulk operation. It will also be a dict with the length of 2. We also print out the Status of the operation and the URL we will follow to get our JSON
bulkOperationCheck=(checkBulkStatus())
print(bulkOperationCheck['data']['currentBulkOperation']['status'])
print(bulkOperationCheck['data']['currentBulkOperation']['url'])

# # We need to follow the link that the bulk operation gives us. Download that link, and then put it into the folder where this application is located. Change the file path to match yours including the file name of the .jsonl file
efJSON = 'THE LOCATION OF THE DOWNLOADED FILE HERE' # Change to match json file name
df = pd.read_json(efJSON, lines = True)
print(df)
df['id'] = df['id'].str.replace('gid://shopify/Customer/', '') # Remove the gid added infront of the ID field 
df.to_csv('THE NAME OF THE EXPORT FILE HERE', encoding='utf-8', index=False) # Here we create our csv file with the data we pulled, change the .csv name here to whatever you want to call the CSV
