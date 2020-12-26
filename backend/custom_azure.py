from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'django491'   # Must be replaced by your <storage_account_name>
    account_key = 'AfsS+FEOse6H57Eo0rO3AjoZ1TZnC54LONQXRMl5q55QxzNTmoq9ynM2KCfClU/rAa+xt9MyAo8GyNETaS/GVA=='     # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'django491'   # Must be replaced by your storage_account_name
    account_key = 'AfsS+FEOse6H57Eo0rO3AjoZ1TZnC54LONQXRMl5q55QxzNTmoq9ynM2KCfClU/rAa+xt9MyAo8GyNETaS/GVA=='    # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None